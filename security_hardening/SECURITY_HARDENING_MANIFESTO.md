# Security Hardening Manifesto: 18 Foundational Principles

**Version**: 2.0
**Classification**: Public
**License**: CC0 - Public Domain
**Standards**: OWASP Top 10, NIST Cybersecurity Framework, CIS Controls, ISO 27001
**Last Updated**: 2025-11-20

---

## Quick Navigation

- **New to security?** → Start with [Learning Paths](#learning-paths) and [Security Maturity Model](#security-maturity-model)
- **Building a security program?** → See [Organizational Enablement](#organizational-enablement) and [Implementation Checklists](#implementation-checklists)
- **Choosing tools?** → Review [Tool Ecosystem Map](#tool-ecosystem-map)
- **Modernizing architecture?** → See [Modern Architecture Considerations](#modern-architecture-considerations)
- **Executive summary** → Review principles overview and [Compliance Mapping](#compliance-mapping)

---

## Core Principles

### I. Defense in Depth
**No single point of failure shall protect a system.**

Implement multiple, independent layers of security controls. If one mechanism fails, others must remain effective. Assume every layer will eventually be breached; design accordingly.

**Layer Strategy:**
- **Network layer**: Firewalls, network segmentation, VPNs, IDS/IPS
- **Application layer**: WAF, API gateway, rate limiting, input validation
- **Identity layer**: MFA, SSO, RBAC, least privilege
- **Data layer**: Encryption at rest, encryption in transit, tokenization, masking
- **Endpoint layer**: EDR, antivirus, application whitelisting, patch management
- **Physical layer**: Access controls, surveillance, environmental controls

**Architecture Pattern:**
```
Internet Traffic
  ↓
[1] CDN/DDoS Protection (Cloudflare, Akamai)
  ↓
[2] WAF (ModSecurity, AWS WAF)
  ↓
[3] Load Balancer with TLS Termination
  ↓
[4] API Gateway (Kong, Apigee) - Rate limiting, JWT validation
  ↓
[5] Application Firewall Rules
  ↓
[6] Application Code - Input validation, CSRF tokens
  ↓
[7] Business Logic - Authorization checks (RBAC/ABAC)
  ↓
[8] Data Access Layer - Parameterized queries, ORM
  ↓
[9] Database - Encrypted at rest, column-level encryption for PII
  ↓
[10] Audit Logs - Tamper-evident, centralized SIEM
```

Each layer operates independently; compromise of one ≠ compromise of all.

**Example Stack (Web Application):**
- Network: VPC with private subnets, security groups, NACLs
- Edge: Cloudflare DDoS protection + WAF
- Application: API Gateway with OAuth2 → Application with CSP headers → Parameterized SQL
- Data: Encrypted RDS with column-level encryption for sensitive fields
- Monitoring: CloudTrail + GuardDuty + Security Hub

**Trade-off**: More layers = more complexity and maintenance overhead. Prioritize layers based on threat model.

---

### II. Least Privilege
**Grant the minimum access required for function; revoke immediately when unnecessary.**

Every process, user, and service operates with the absolute minimum permissions needed. Default deny; explicitly allow. Temporary elevations expire automatically.

- `rwx------` over `rwxrwxrwx`
- Service accounts ≠ administrative rights
- Time-bounded credentials with automatic revocation
- Just-in-time (JIT) privileged access
- Regular access reviews (quarterly minimum)

**Implementation Patterns:**

**User Access:**
```
Role: Developer
Permissions:
  - Read: production logs (filtered, no PII)
  - Write: development environment
  - Denied: production database access, IAM policy changes

Temporary Elevation (break-glass):
  - Request: incident response access
  - Approval: manager + security team
  - Duration: 4 hours
  - Automatic revocation: yes
  - Audit: all actions logged with justification
```

**Service Account:**
```
Service: order-processor
Permissions:
  - Read: orders table
  - Write: order_status field only
  - Denied: customer_credit_card field, user table
  - Network: access only to payment API, no internet egress
```

**AWS IAM Policy Example:**
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject"],
    "Resource": ["arn:aws:s3:::my-bucket/public/*"],
    "Condition": {
      "IpAddress": {
        "aws:SourceIp": ["10.0.0.0/8"]
      }
    }
  }]
}
```

**Enforcement:**
- Privileged Access Management (PAM) tools: CyberArk, BeyondTrust
- Cloud IAM: AWS IAM, Azure RBAC, GCP IAM
- Kubernetes: RBAC, Pod Security Policies/Standards
- Database: column-level permissions, row-level security

---

### III. Fail Secure
**System failure shall not compromise security posture.**

When errors occur, default to the most secure state. Failures close connections, deny access, and preserve audit logs. Never fail open.

- Exception → deny access, log attempt, alert
- Resource exhaustion → graceful degradation with maintained security
- Invalid state → halt rather than proceed insecurely
- Authentication service down → deny access, not bypass auth
- Authorization cache stale → revalidate, not assume previous state

**Examples:**

**Database Connection Failure:**
```python
# BAD: Fail open
try:
    user = db.get_user(user_id)
    if user.is_admin:
        return allow_access()
except DatabaseError:
    # Assume admin if DB is down - DANGEROUS
    return allow_access()

# GOOD: Fail secure
try:
    user = db.get_user(user_id)
    if user.is_admin:
        return allow_access()
except DatabaseError as e:
    log.error(f"Database failure during authz check: {e}")
    alert_security_team("Authorization system failure")
    return deny_access(reason="system_unavailable")
```

**Rate Limiter Failure:**
```python
# BAD: Disable rate limiting if Redis is down
try:
    rate_limiter.check(user_id)
except RedisConnectionError:
    pass  # Allow request - DANGEROUS

# GOOD: Fail closed
try:
    rate_limiter.check(user_id)
except RedisConnectionError as e:
    log.error(f"Rate limiter unavailable: {e}")
    # Use local in-memory rate limiting as fallback
    return local_rate_limiter.check(user_id)
```

**Certificate Validation:**
```python
# BAD: Skip validation on error
try:
    verify_certificate(server_cert)
except ValidationError:
    # Continue anyway - DANGEROUS
    proceed_with_connection()

# GOOD: Reject on validation failure
try:
    verify_certificate(server_cert)
except ValidationError as e:
    log.error(f"Certificate validation failed: {e}")
    raise ConnectionRefusedError("Invalid server certificate")
```

**Circuit Breaker Pattern:**
When downstream service failures occur, circuit breaker prevents cascading failures while maintaining security:
```
Closed (normal) → requests flow, failures tracked
  ↓ (threshold exceeded)
Open (failing) → requests denied immediately (fail secure)
  ↓ (timeout expires)
Half-Open (testing) → limited requests allowed
  ↓ (success) → Closed OR (failure) → Open
```

---

### IV. Complete Mediation
**Every access to every resource must be checked against access control policy.**

No cached permissions. No shortcuts. Every request validated against current authorization state at time of access.

- Verify on each operation, not once per session
- No "already authenticated" assumptions for state-changing operations
- Fresh validation for sensitive operations (privilege escalation, data export)
- Token expiration enforced strictly

**Examples:**

**Session-Based Auth (Bad Pattern):**
```python
# BAD: Check permissions once at login
@app.route('/login')
def login():
    user = authenticate(username, password)
    session['is_admin'] = user.is_admin  # Set once
    return redirect('/dashboard')

@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    if session.get('is_admin'):  # Trust session, never revalidate
        User.delete(user_id)
```
**Problem**: If user's admin status is revoked, session still claims admin until logout.

**Complete Mediation (Good Pattern):**
```python
# GOOD: Check permissions on every request
@app.route('/delete_user/<user_id>')
@require_permission('user:delete')
def delete_user(user_id):
    # Permission decorator validates against current user state
    User.delete(user_id)

def require_permission(permission):
    def decorator(f):
        def wrapper(*args, **kwargs):
            user = get_current_user()  # Fresh DB lookup
            if not user.has_permission(permission):
                log_authz_failure(user, permission)
                abort(403)
            return f(*args, **kwargs)
        return wrapper
    return decorator
```

**Token-Based Auth:**
```python
# GOOD: Validate token on every request
@app.before_request
def validate_token():
    token = request.headers.get('Authorization')
    try:
        # Verify signature, expiration, revocation status
        claims = jwt.decode(token, public_key, algorithms=['RS256'])

        # Check token revocation list (for logout/password change)
        if redis.exists(f"revoked:{claims['jti']}"):
            abort(401, "Token revoked")

        # Attach user context
        g.user_id = claims['sub']
    except jwt.ExpiredSignatureError:
        abort(401, "Token expired")
    except jwt.InvalidTokenError:
        abort(401, "Invalid token")
```

**Caching Strategy (When Performance Critical):**
If complete mediation is too expensive, use short-lived caches with explicit invalidation:
```python
@cache(ttl=60)  # Cache for 60 seconds max
def get_user_permissions(user_id):
    return db.query("SELECT permissions FROM users WHERE id = ?", user_id)

# Invalidate cache on permission change
def update_user_permissions(user_id, new_permissions):
    db.execute("UPDATE users SET permissions = ? WHERE id = ?",
               new_permissions, user_id)
    cache.delete(f"user_permissions:{user_id}")
```

**Trade-off**: Performance vs. security. For high-security operations (financial transactions, admin actions), always use complete mediation. For read-only operations, short caches acceptable.

---

### V. Economy of Mechanism
**Security mechanisms shall be simple, small, and verifiable.**

Complexity is the enemy of security. Simple systems are auditable, testable, and comprehensible. Minimize trusted computing base (TCB).

- Fewer lines of security-critical code → fewer vulnerabilities
- Prefer proven primitives over custom implementations
- `authenticate() → bool` over elaborate multi-stage ceremonies
- Use standard libraries for crypto, auth, encoding
- Reduce attack surface by removing unnecessary features

**Examples:**

**Authentication (Bad - Complex):**
```python
def authenticate(username, password):
    # Custom crypto, complex logic, hard to audit
    salt = custom_salt_generator(username)
    hash1 = custom_hash_v1(password, salt)
    hash2 = custom_hash_v2(hash1, secret_key)
    obfuscated = custom_obfuscation(hash2)
    stored = db.get_hash(username)
    if custom_compare(obfuscated, stored):
        if custom_time_check():
            if custom_rate_limit():
                return custom_token_generator(username)
    return None
```
**Problems**: Custom crypto (likely broken), complex flow (bugs), hard to audit.

**Authentication (Good - Simple):**
```python
import bcrypt
import secrets

def authenticate(username, password):
    user = db.get_user(username)
    if user is None:
        return None

    # Use proven library (bcrypt)
    if bcrypt.checkpw(password.encode(), user.password_hash):
        # Use cryptographically secure token generation
        token = secrets.token_urlsafe(32)
        db.save_session(user.id, token, expiry=3600)
        return token
    return None
```
**Benefits**: Standard crypto library, clear logic, easy to audit, fewer bugs.

**Access Control (Prefer Simple Models):**
- **Simple**: RBAC (Role-Based Access Control) - Users → Roles → Permissions
- **Complex**: ABAC (Attribute-Based Access Control) - Policies with arbitrary attributes

Start with RBAC; move to ABAC only when necessary.

**Minimize TCB:**
```
Bad TCB (large attack surface):
  Application (100K LOC) + Web Framework (50K LOC) +
  OS (5M LOC) + Database (1M LOC) = ~6.15M LOC to trust

Better TCB (reduced):
  Security-critical module (5K LOC) +
  Crypto library (10K LOC) +
  Microkernel (10K LOC) = ~25K LOC to trust
```

**Practical Application:**
- Use OAuth2 instead of building custom auth
- Use TLS instead of custom encryption protocols
- Use prepared statements instead of manual SQL escaping
- Use CSP headers instead of complex XSS filters

---

### VI. Secure by Default
**Initial configuration shall be maximally secure; users must explicitly relax constraints.**

Ship with security enabled. Require conscious, documented decisions to reduce protection. Never ship with default credentials.

- TLS enforced; HTTP disabled by default
- Authentication mandatory; anonymous access requires explicit flag
- Encryption at rest enabled; plaintext requires override
- Security headers enabled (CSP, HSTS, X-Frame-Options)
- Debug mode disabled in production
- Verbose errors disabled (leak no information)
- CORS restricted (not `Access-Control-Allow-Origin: *`)
- File uploads disabled or tightly restricted
- Default passwords prohibited

**Examples:**

**Web Framework Configuration:**
```python
# Good: Secure defaults
app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.environ['SECRET_KEY'],  # Required, not default
    SESSION_COOKIE_SECURE=True,  # HTTPS only
    SESSION_COOKIE_HTTPONLY=True,  # No JavaScript access
    SESSION_COOKIE_SAMESITE='Lax',  # CSRF protection
    PERMANENT_SESSION_LIFETIME=3600,  # 1 hour max
    MAX_CONTENT_LENGTH=16 * 1024 * 1024,  # 16 MB upload limit
    DEBUG=False  # Never true in production
)

# Force HTTPS
@app.before_request
def enforce_https():
    if not request.is_secure:
        return redirect(request.url.replace('http://', 'https://'), 301)
```

**Database Configuration:**
```sql
-- Good: Secure defaults
CREATE USER app_user WITH PASSWORD 'random_generated_password';
GRANT SELECT, INSERT, UPDATE ON orders TO app_user;
-- No DELETE, no DROP, no GRANT
-- No default password like 'password123'

-- Encryption at rest enabled
ALTER DATABASE mydb SET encryption = 'on';

-- Audit logging enabled
ALTER DATABASE mydb SET log_statement = 'mod';  -- Log all modifications
```

**API Configuration:**
```yaml
# Good: Secure defaults in Kubernetes
apiVersion: v1
kind: Pod
spec:
  securityContext:
    runAsNonRoot: true  # Don't run as root
    runAsUser: 1000
    fsGroup: 1000
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: myapp:latest
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true  # Immutable container
      capabilities:
        drop: ["ALL"]  # Drop all capabilities
    resources:
      limits:
        memory: "512Mi"
        cpu: "500m"
    env:
    - name: DEBUG
      value: "false"  # No debug mode
```

**Deployment Checklist:**
- [ ] No default credentials (admin/admin, root/password)
- [ ] TLS certificate configured (not self-signed)
- [ ] Security headers enabled
- [ ] Debug/verbose logging disabled
- [ ] Unnecessary services disabled (telnet, FTP, SMB)
- [ ] Firewall rules default-deny
- [ ] File permissions restrictive (not 777)

---

### VII. Zero Trust
**Trust nothing. Verify everything. Assume breach.**

No implicit trust based on network location. Authenticate and authorize every request. Segment networks; inspect encrypted traffic at boundaries.

- Internal requests = external requests in terms of verification
- "Inside the firewall" ≠ trusted
- Continuous verification, not perimeter-based security
- Microsegmentation: limit lateral movement
- Device posture checking before access

**Zero Trust Architecture Components:**

**1. Identity-Based Access (Not Network-Based):**
```
Traditional (Perimeter):
  Outside network → DENY
  Inside network → ALLOW (implicit trust)

Zero Trust:
  Every request → Authenticate + Authorize (regardless of network)
```

**2. Mutual TLS (mTLS) for Service-to-Service:**
```yaml
# Service mesh (Istio) enforces mTLS
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
spec:
  mtls:
    mode: STRICT  # Require mTLS for all service communication
```

**3. Continuous Authentication:**
```python
# Re-authenticate for sensitive operations
@app.route('/transfer_money')
def transfer_money():
    # User already authenticated with session
    # But require step-up auth for sensitive operation
    if not session.get('mfa_verified_at') or \
       (time.time() - session['mfa_verified_at']) > 300:  # 5 min
        return redirect('/verify_mfa')

    # Proceed with transaction
    process_transfer()
```

**4. Network Microsegmentation:**
```
Traditional flat network:
  [Web] ←→ [App] ←→ [DB] ←→ [HR System] ←→ [Finance System]
  (Compromise of Web → access to HR and Finance)

Microsegmented:
  [Web] → [App] → [DB]
  [HR App] → [HR DB]
  [Finance App] → [Finance DB]
  (Firewall rules: Web can ONLY talk to App, App can ONLY talk to DB)
```

**5. Device Trust (Posture Checking):**
```python
# BeyondCorp model: Verify device before granting access
def check_device_posture(device_id):
    device = get_device_info(device_id)

    checks = [
        device.os_version_up_to_date(),
        device.antivirus_running(),
        device.disk_encrypted(),
        device.screen_lock_enabled(),
        not device.jailbroken(),
        device.certificate_valid()
    ]

    if not all(checks):
        return deny_access(reason="device_posture_failed")

    return allow_access()
```

**Implementation Path:**
1. **Phase 1**: Implement strong authentication (MFA everywhere)
2. **Phase 2**: Deploy identity-aware proxy (Google BeyondCorp, Palo Alto Prisma Access)
3. **Phase 3**: Enable mTLS for service mesh
4. **Phase 4**: Implement microsegmentation (network policies)
5. **Phase 5**: Continuous monitoring and adaptive policies

**Tools:**
- Identity-aware proxy: Pomerium, oauth2-proxy, Google IAP
- Service mesh: Istio, Linkerd, Consul Connect
- Network policies: Kubernetes Network Policies, AWS Security Groups, Calico
- Device trust: Duo, Okta, Azure AD Conditional Access

---

### VIII. Cryptographic Agility
**Cryptographic primitives shall be replaceable without architectural redesign.**

Abstract cryptographic operations. Prepare for algorithm obsolescence. Version all encrypted data with algorithm metadata.

- `encrypt(data, algorithm_id)` not `aes_encrypt(data)`
- Store: `{v:2, alg:"ChaCha20-Poly1305", data:...}`
- Rotate algorithms without full data migration when possible
- Prepare for quantum-resistant cryptography

**Design Pattern:**

**Bad (Tightly Coupled):**
```python
def encrypt_user_data(data):
    # Hardcoded algorithm, no version
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(data))

def decrypt_user_data(encrypted):
    # Assumes AES-CBC forever
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted))
```
**Problem**: Cannot change algorithm without breaking all existing encrypted data.

**Good (Cryptographic Agility):**
```python
from enum import Enum

class CryptoAlgorithm(Enum):
    AES_256_GCM = 1
    CHACHA20_POLY1305 = 2
    AES_256_GCM_SIV = 3  # Future algorithm

CURRENT_ALGORITHM = CryptoAlgorithm.CHACHA20_POLY1305

def encrypt(data: bytes, algorithm: CryptoAlgorithm = CURRENT_ALGORITHM) -> dict:
    if algorithm == CryptoAlgorithm.AES_256_GCM:
        cipher = AES.new(get_key(algorithm), AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return {
            'version': 1,
            'algorithm': 'AES-256-GCM',
            'nonce': b64encode(cipher.nonce).decode(),
            'tag': b64encode(tag).decode(),
            'ciphertext': b64encode(ciphertext).decode()
        }
    elif algorithm == CryptoAlgorithm.CHACHA20_POLY1305:
        cipher = ChaCha20_Poly1305.new(key=get_key(algorithm))
        ciphertext = cipher.encrypt_and_digest(data)
        return {
            'version': 2,
            'algorithm': 'ChaCha20-Poly1305',
            'nonce': b64encode(cipher.nonce).decode(),
            'tag': b64encode(tag).decode(),
            'ciphertext': b64encode(ciphertext).decode()
        }

def decrypt(encrypted_obj: dict) -> bytes:
    # Route to correct algorithm based on version
    algorithm = encrypted_obj['algorithm']

    if algorithm == 'AES-256-GCM':
        return decrypt_aes_gcm(encrypted_obj)
    elif algorithm == 'ChaCha20-Poly1305':
        return decrypt_chacha20(encrypted_obj)
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")
```

**Algorithm Migration Strategy:**
```python
# Step 1: Deploy new encryption algorithm for new data
CURRENT_ALGORITHM = CryptoAlgorithm.CHACHA20_POLY1305

# Step 2: Background job re-encrypts old data
def migrate_encryption(user_id):
    user_data = db.get_encrypted_data(user_id)

    if user_data['algorithm'] == 'AES-256-GCM':
        # Decrypt with old algorithm
        plaintext = decrypt(user_data)
        # Re-encrypt with new algorithm
        new_encrypted = encrypt(plaintext, CryptoAlgorithm.CHACHA20_POLY1305)
        db.update_encrypted_data(user_id, new_encrypted)

# Step 3: Once migration complete (months later), remove old algorithm support
```

**TLS Cipher Suite Agility:**
```nginx
# nginx configuration with ordered cipher preference
ssl_protocols TLSv1.3 TLSv1.2;  # No TLS 1.0/1.1
ssl_ciphers 'TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:ECDHE-RSA-AES256-GCM-SHA384';
ssl_prefer_server_ciphers on;

# Easy to update when new ciphers emerge
```

**Quantum Resistance Preparation:**
```python
# Hybrid approach: Classical + Post-Quantum
def encrypt_quantum_safe(data):
    # Use both classical and PQ algorithms
    # Compromise requires breaking BOTH
    classical_encrypted = encrypt(data, CryptoAlgorithm.CHACHA20_POLY1305)
    pq_encrypted = encrypt(classical_encrypted, CryptoAlgorithm.KYBER_1024)
    return pq_encrypted
```

**Key Rotation:**
```python
# Support multiple active keys for gradual rotation
class KeyManager:
    def __init__(self):
        self.keys = {
            1: Key(id=1, created='2024-01-01', status='retired'),
            2: Key(id=2, created='2024-06-01', status='active'),
            3: Key(id=3, created='2024-11-01', status='active')  # New key
        }
        self.primary_key_id = 3

    def encrypt(self, data):
        # Always use latest key
        return encrypt_with_key(data, self.keys[self.primary_key_id])

    def decrypt(self, encrypted_obj):
        # Support decryption with any active/retired key
        key_id = encrypted_obj['key_id']
        return decrypt_with_key(encrypted_obj, self.keys[key_id])
```

---

### IX. Secure Development Lifecycle (SDL)
**Security integrated at every phase; never bolted on post-facto.**

Threat modeling before design. Security requirements alongside functional requirements. Automated security testing in CI/CD. Regular penetration testing.

**SDL Phases:**

**1. Requirements Phase:**
- Security requirements documented alongside functional requirements
- Compliance requirements identified (PCI-DSS, HIPAA, GDPR)
- Data classification and handling requirements
- Authentication and authorization requirements

**2. Design Phase:**
- **Threat modeling** (STRIDE, PASTA, LINDDUN)
- Trust boundaries identified
- Data flow diagrams (DFDs) created
- Attack surface analysis
- Cryptographic requirements specified
- Abuse cases documented alongside use cases

**Threat Modeling Example (STRIDE):**
```
Feature: Password Reset

Threats:
[S] Spoofing: Attacker requests password reset for victim's email
    Mitigation: Send reset link to registered email, require email verification

[T] Tampering: Attacker modifies reset token in URL
    Mitigation: HMAC-signed tokens, single-use, time-limited (15 minutes)

[R] Repudiation: User claims they didn't reset password
    Mitigation: Log all password reset events with IP, timestamp, user agent

[I] Information Disclosure: Reset token in URL logged/cached
    Mitigation: POST-based reset (not GET), no-cache headers

[D] Denial of Service: Attacker floods reset requests
    Mitigation: Rate limiting (3 requests per hour per email)

[E] Elevation of Privilege: Reset token for user A works for user B
    Mitigation: Token cryptographically bound to user ID
```

**3. Implementation Phase:**
- Secure coding guidelines followed (OWASP, CERT)
- Code review with security checklist
- Peer review required (2-person rule for security-critical code)
- Static Application Security Testing (SAST) in IDE
- Pre-commit hooks for secret detection

**4. Verification Phase (Testing):**
- **Unit tests**: Security-focused test cases
- **SAST**: SonarQube, Semgrep, CodeQL
- **DAST**: OWASP ZAP, Burp Suite
- **SCA**: Dependency scanning (Snyk, Dependabot)
- **IaC scanning**: Checkov, tfsec, Terrascan
- **Container scanning**: Trivy, Clair, Anchore
- **Secrets scanning**: TruffleHog, GitLeaks, detect-secrets
- **Fuzz testing**: AFL, libFuzzer, OSS-Fuzz

**5. Release Phase:**
- Security sign-off required (Security Champion or AppSec team)
- Penetration testing for high-risk releases
- Security-focused acceptance criteria must pass
- Deployment approval workflow (separation of duties)

**6. Operations/Maintenance Phase:**
- Runtime Application Self-Protection (RASP)
- Security monitoring and logging (SIEM integration)
- Incident response playbooks ready
- Regular vulnerability scanning
- Patch management within SLA

**CI/CD Security Pipeline:**
```yaml
# .github/workflows/security.yml
name: Security Checks

on: [push, pull_request]

jobs:
  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Semgrep
        run: semgrep --config=auto --error

  secrets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Detect secrets
        run: |
          pip install detect-secrets
          detect-secrets scan --baseline .secrets.baseline

  dependencies:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Scan dependencies
        run: |
          pip install safety
          safety check --json

  container:
    runs-on: ubuntu-latest
    steps:
      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .
      - name: Scan image
        run: |
          docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
            aquasec/trivy image --severity HIGH,CRITICAL myapp:${{ github.sha }}

  dast:
    runs-on: ubuntu-latest
    steps:
      - name: ZAP Scan
        run: |
          docker run -v $(pwd):/zap/wrk/:rw \
            owasp/zap2docker-stable zap-baseline.py \
            -t https://staging.example.com -r report.html
```

**Security Champions Program:**
- Embed security champions in each product team
- Training: OWASP Top 10, secure coding, threat modeling
- Responsibilities: Security review, promoting best practices, liaison with AppSec team
- Recognition: Certifications, bonuses, career advancement

**SDL Maturity Levels:**

**Level 0 - Ad Hoc**: No formal SDL, security as afterthought
**Level 1 - Opportunistic**: Some security activities, inconsistent
**Level 2 - Repeatable**: Security checklist, basic automation
**Level 3 - Defined**: Formal SDL process, security gates, training
**Level 4 - Managed**: Metrics-driven, continuous improvement
**Level 5 - Optimizing**: Industry-leading, proactive threat research

---

### X. Audit Everything
**All security-relevant events shall be logged immutably with sufficient context for investigation.**

Log authentication attempts, authorization decisions, configuration changes, and data access. Timestamps, source, actor, action, outcome. Tamper-evident storage.

**What to Log:**

**1. Authentication Events:**
- Login attempts (success and failure)
- Logout events
- Password changes/resets
- MFA enrollment/verification
- Session creation/expiration
- Account lockouts

**2. Authorization Events:**
- Permission grants/revocations
- Role assignments
- Access denials (403 Forbidden)
- Privilege escalation attempts

**3. Data Access:**
- Read access to sensitive data (PII, financial, health)
- Data modifications (create, update, delete)
- Data exports/downloads
- Bulk operations

**4. Configuration Changes:**
- Security policy updates
- User/role management
- System configuration changes
- Firewall rule changes
- Cryptographic key operations

**5. Security Events:**
- Malware detection
- Intrusion attempts
- Rate limit violations
- Suspicious patterns (SQL injection attempts, XSS)

**Structured Logging Format:**
```json
{
  "timestamp": "2025-11-20T15:32:01.543Z",
  "event_id": "evt_7x9k2m3p",
  "event_type": "authorization.denied",
  "severity": "WARNING",
  "actor": {
    "user_id": "usr_abc123",
    "username": "john.doe@example.com",
    "ip_address": "203.0.113.42",
    "user_agent": "Mozilla/5.0...",
    "session_id": "sess_xyz789"
  },
  "resource": {
    "type": "document",
    "id": "doc_secret_42",
    "classification": "confidential"
  },
  "action": "READ",
  "result": "DENIED",
  "reason": "insufficient_privileges",
  "required_permission": "documents:read:confidential",
  "user_permissions": ["documents:read:public", "documents:read:internal"],
  "trace_id": "trace_abc123def456",
  "span_id": "span_789ghi012"
}
```

**Log Attributes (Minimum):**
- **Timestamp**: ISO 8601 with timezone (UTC)
- **Event ID**: Unique identifier
- **Actor**: Who (user ID, IP, session)
- **Action**: What (READ, WRITE, DELETE, LOGIN)
- **Resource**: Which object (document ID, API endpoint)
- **Result**: Success or failure
- **Reason**: Why (for failures)
- **Trace ID**: Correlation across services
- **Severity**: INFO, WARNING, ERROR, CRITICAL

**Tamper-Evident Logging:**
```python
# Append-only logs with cryptographic integrity
class TamperEvidentLog:
    def __init__(self):
        self.log_chain = []
        self.previous_hash = "0" * 64  # Genesis block

    def append(self, event):
        entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'event': event,
            'previous_hash': self.previous_hash,
            'hash': None  # Computed below
        }

        # Compute hash of entry
        entry_str = json.dumps(entry, sort_keys=True)
        entry['hash'] = hashlib.sha256(entry_str.encode()).hexdigest()

        # Update chain
        self.previous_hash = entry['hash']
        self.log_chain.append(entry)

        # Send to immutable storage (S3, blockchain, WORM)
        self.store(entry)

    def verify_integrity(self):
        # Verify chain hasn't been tampered with
        prev_hash = "0" * 64
        for entry in self.log_chain:
            if entry['previous_hash'] != prev_hash:
                return False
            # Recompute hash and verify
            computed_hash = self.compute_hash(entry)
            if computed_hash != entry['hash']:
                return False
            prev_hash = entry['hash']
        return True
```

**Log Retention:**
```
Event Type              Retention   Storage Tier
--------------------------------------------------
Authentication          1 year      Hot (searchable)
Authorization denials   2 years     Warm (archive after 3 months)
Data access (PII)       7 years     Cold (legal requirement)
Configuration changes   Indefinite  Warm
Security incidents      Indefinite  Hot
```

**Privacy Considerations:**
- **PII in logs**: Hash or redact sensitive fields
- **GDPR Right to Erasure**: Pseudonymization strategy (separate key vault)
- **Log access controls**: Audit logs are sensitive, restrict access

**Centralized Logging (SIEM):**
```
Application Servers → Log Shipper (Fluentd, Filebeat)
                              ↓
                    Log Aggregator (Kafka, Kinesis)
                              ↓
                    SIEM (Splunk, ELK, Datadog)
                              ↓
                    Analysis + Alerting
```

**Alerting Rules:**
```yaml
# Example: Alert on repeated authentication failures
alert: BruteForceDetection
expr: |
  count_over_time(
    {event_type="authentication.failed"}[5m]
  ) by (actor.ip_address) > 10
severity: HIGH
notification: security-team@example.com
action: auto-block IP for 1 hour
```

**Forensic Readiness:**
- Logs preserved for incident investigation
- Disk snapshots/backups for forensic analysis
- Chain of custody procedures for legal evidence

---

### XI. Separation of Duties
**No single actor shall have sufficient privileges to subvert critical operations.**

Require multiple independent actors for sensitive operations. Split cryptographic keys. Dual control for administrative functions.

- Deployment requires: code review + security review + operations approval
- Key recovery: M-of-N threshold schemes
- Financial transactions: initiator ≠ approver

**Implementation Patterns:**

**1. Code Deployment (4-Eyes Principle):**
```yaml
# GitHub branch protection rules
branches:
  - name: main
    protection:
      required_pull_request_reviews:
        required_approving_review_count: 2
        dismiss_stale_reviews: true
        require_code_owner_reviews: true
      required_status_checks:
        strict: true
        contexts:
          - security/sast
          - security/secrets-scan
          - security/dependency-check
      enforce_admins: true
      restrictions:
        users: []
        teams: ["security-team", "ops-team"]
```

**Approval workflow**:
1. Developer submits PR
2. Peer review approval (another developer)
3. Security champion approval (if security-critical)
4. Automated checks pass (SAST, tests)
5. Merge allowed
6. Deployment approval (ops team, separate from dev)

**2. Infrastructure Changes (Dual Control):**
```python
# Terraform/infrastructure changes require approval
class InfrastructureChange:
    def apply(self, change):
        # Author cannot approve their own change
        if change.author == current_user:
            raise PermissionError("Cannot approve own change")

        # Require 2 approvals from different teams
        approvals = change.get_approvals()
        teams = {a.approver.team for a in approvals}

        if len(approvals) < 2 or len(teams) < 2:
            raise PermissionError("Need 2 approvals from different teams")

        # Apply change
        terraform_apply(change)
        audit_log(f"Infrastructure change {change.id} applied", approvals)
```

**3. Financial Transactions (Maker-Checker):**
```python
class WireTransfer:
    def initiate(self, amount, recipient):
        # Maker: Initiates transaction
        transfer = Transfer(
            amount=amount,
            recipient=recipient,
            status='PENDING_APPROVAL',
            initiator=current_user
        )
        db.save(transfer)
        notify_approvers(transfer)
        return transfer

    def approve(self, transfer_id):
        # Checker: Approves transaction
        transfer = db.get_transfer(transfer_id)

        # Initiator cannot approve
        if transfer.initiator == current_user:
            raise PermissionError("Cannot approve own transfer")

        # Large amounts require multiple approvals
        required_approvals = 1 if transfer.amount < 10000 else 2

        if len(transfer.approvals) + 1 >= required_approvals:
            transfer.status = 'APPROVED'
            execute_transfer(transfer)
        else:
            transfer.approvals.append(current_user)

        db.save(transfer)
```

**4. Cryptographic Key Management (M-of-N):**
```python
# Shamir's Secret Sharing: Require 3 of 5 keyholders to recover master key
from secretsharing import PlaintextToHexSecretSharer

def split_master_key(master_key, threshold=3, num_shares=5):
    # Split key into 5 shares, any 3 can reconstruct
    shares = PlaintextToHexSecretSharer.split_secret(master_key, threshold, num_shares)

    # Distribute to different keyholders
    # (different geographic locations, different people)
    distribute_shares(shares)

    return shares

def recover_master_key(share_1, share_2, share_3):
    # Require physical presence of 3 keyholders
    # (e.g., disaster recovery scenario)
    master_key = PlaintextToHexSecretSharer.recover_secret([share_1, share_2, share_3])

    audit_log("Master key recovered", keyholders=[share_1.holder, share_2.holder, share_3.holder])

    return master_key
```

**5. Database Schema Changes:**
```
DBA1: Writes migration script
  ↓
DBA2: Reviews migration script
  ↓
Security: Reviews for access control implications
  ↓
QA: Tests in staging environment
  ↓
DBA3: Executes in production (different from DBA1)
  ↓
Audit: All steps logged with approvals
```

**6. Production Access (Break-Glass):**
```python
class ProductionAccess:
    def request_access(self, reason, duration):
        request = AccessRequest(
            user=current_user,
            reason=reason,
            duration=duration,
            status='PENDING'
        )

        # Requires manager approval
        notify_manager(current_user.manager, request)

        # Requires security team approval for sensitive systems
        if current_user.role in ['developer', 'contractor']:
            notify_security_team(request)

        return request

    def approve_access(self, request_id):
        request = db.get_access_request(request_id)

        # Approver cannot be requester
        if request.user == current_user:
            raise PermissionError("Cannot approve own access request")

        # Grant temporary access
        grant_temporary_access(
            user=request.user,
            duration=request.duration,
            resources=['production-database']
        )

        # Schedule automatic revocation
        schedule_revocation(request.user, after=request.duration)

        # Alert on all actions taken
        monitor_user_actions(request.user, alert_threshold='any_action')
```

**Separation of Duties Matrix:**

| Role | Deploy Code | Approve Code | Modify IAM | Approve IAM | Access Prod DB | Approve DB Access |
|------|-------------|--------------|------------|-------------|----------------|-------------------|
| Developer | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Senior Dev | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| Security | ✗ | ✓ | ✓ | ✗ | ✗ | ✓ |
| Ops | ✗ | ✓ | ✓ | ✗ | Request only | ✓ |
| Manager | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ |

**Trade-off**: Separation of duties adds process overhead. Balance security with velocity based on risk.

---

### XII. Input Validation & Output Encoding
**Validate all inputs against strict schemas; encode all outputs for destination context.**

Never trust data crossing trust boundaries. Whitelist acceptable input; reject malformed data at boundary. Context-aware output encoding prevents injection.

**Input Validation:**

**1. Validation Principles:**
- **Whitelist over blacklist**: Define what IS allowed, not what ISN'T
- **Validate at boundary**: As early as possible
- **Strict typing**: Enforce data types
- **Canonicalization**: Normalize before validation (prevent bypass)
- **Length limits**: Prevent DoS
- **Regular expression safety**: Avoid ReDoS

**2. Input Validation Layers:**

**API Gateway Layer:**
```yaml
# OpenAPI schema validation
paths:
  /api/users:
    post:
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [email, password, age]
              properties:
                email:
                  type: string
                  format: email
                  maxLength: 255
                password:
                  type: string
                  minLength: 12
                  maxLength: 128
                age:
                  type: integer
                  minimum: 13
                  maximum: 120
```

**Application Layer:**
```python
from pydantic import BaseModel, EmailStr, constr, validator
import re

class UserRegistration(BaseModel):
    email: EmailStr  # Validates email format
    password: constr(min_length=12, max_length=128)
    username: constr(regex=r'^[a-zA-Z0-9_-]{3,20}$')  # Alphanumeric, 3-20 chars
    age: int

    @validator('age')
    def validate_age(cls, v):
        if not (13 <= v <= 120):
            raise ValueError('Age must be between 13 and 120')
        return v

    @validator('password')
    def validate_password_strength(cls, v):
        # At least one uppercase, one lowercase, one digit, one special
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain digit')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError('Password must contain special character')
        return v

# Usage
@app.route('/register', methods=['POST'])
def register():
    try:
        user_data = UserRegistration(**request.json)
        # Data is validated, safe to use
        create_user(user_data)
    except ValidationError as e:
        return jsonify({'errors': e.errors()}), 400
```

**3. File Upload Validation:**
```python
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

def validate_file_upload(file):
    # Check file extension
    if '.' not in file.filename:
        raise ValidationError("No file extension")

    ext = file.filename.rsplit('.', 1)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValidationError(f"Invalid file type: {ext}")

    # Check file size
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)  # Reset to beginning
    if file_size > MAX_FILE_SIZE:
        raise ValidationError(f"File too large: {file_size} bytes")

    # Check magic bytes (not just extension)
    import magic
    mime_type = magic.from_buffer(file.read(2048), mime=True)
    file.seek(0)

    allowed_mimes = {'image/png', 'image/jpeg', 'application/pdf'}
    if mime_type not in allowed_mimes:
        raise ValidationError(f"Invalid file content: {mime_type}")

    # Scan for malware
    scan_result = antivirus_scan(file)
    if not scan_result.is_clean:
        raise SecurityError("Malware detected")

    # Store in sandboxed location (not web-accessible)
    safe_filename = secure_filename(file.filename)
    file.save(f'/var/uploads/{uuid4()}/{safe_filename}')
```

**4. SQL Injection Prevention:**
```python
# BAD: String concatenation
username = request.form['username']
query = f"SELECT * FROM users WHERE username = '{username}'"  # VULNERABLE
cursor.execute(query)

# GOOD: Parameterized queries
username = request.form['username']
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))  # Safe
```

**Output Encoding:**

**1. Context-Aware Encoding:**

**HTML Context:**
```python
import html

username = user.get_username()  # May contain malicious content

# Bad
output = f"<p>Welcome, {username}!</p>"  # XSS vulnerability

# Good
output = f"<p>Welcome, {html.escape(username)}!</p>"
# <p>Welcome, &lt;script&gt;alert(1)&lt;/script&gt;</p>
```

**JavaScript Context:**
```python
import json

user_data = get_user_data()

# Bad
output = f"<script>var user = {user_data};</script>"  # Unsafe

# Good
output = f"<script>var user = {json.dumps(user_data)};</script>"
```

**URL Context:**
```python
from urllib.parse import quote

search_term = request.args.get('q')

# Bad
redirect_url = f"/search?q={search_term}"  # Can break URL parsing

# Good
redirect_url = f"/search?q={quote(search_term)}"
```

**SQL Context** (use parameterization, not encoding):
```python
# Don't manually escape - use ORM or parameterized queries
```

**2. Content Security Policy (CSP):**
```python
@app.after_request
def set_security_headers(response):
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' https://cdn.example.com; "
        "style-src 'self' 'unsafe-inline'; "  # Avoid 'unsafe-inline' if possible
        "img-src 'self' data: https:; "
        "font-src 'self' https://fonts.gstatic.com; "
        "connect-src 'self' https://api.example.com; "
        "frame-ancestors 'none'; "
        "base-uri 'self'; "
        "form-action 'self'"
    )
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
```

**3. CORS Configuration:**
```python
# Bad: Allow all origins
@app.after_request
def cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # DANGEROUS
    return response

# Good: Whitelist specific origins
ALLOWED_ORIGINS = ['https://app.example.com', 'https://mobile.example.com']

@app.after_request
def cors(response):
    origin = request.headers.get('Origin')
    if origin in ALLOWED_ORIGINS:
        response.headers['Access-Control-Allow-Origin'] = origin
        response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response
```

**4. Regular Expression DoS (ReDoS) Prevention:**
```python
# Bad: Vulnerable to ReDoS
pattern = r'^(a+)+$'
re.match(pattern, 'a' * 30 + '!')  # Takes exponential time

# Good: Use atomic groups or possessive quantifiers
pattern = r'^(?:a+)+$'  # Atomic group
# Or better: validate without complex regex
```

**Defense in Depth for Injection:**
1. **Input validation**: Reject malformed input
2. **Output encoding**: Escape for context
3. **Parameterized queries**: For SQL
4. **CSP**: For XSS
5. **WAF**: As last line of defense

---

### XIII. Secure Secrets Management
**Secrets never appear in code, logs, or version control; access is audited and time-limited.**

Centralized secrets management with encryption, access controls, rotation policies, and audit logs. Secrets injected at runtime; never persisted in application artifacts.

**What Are Secrets:**
- Passwords, API keys, tokens
- Private keys, certificates
- Database credentials
- Encryption keys
- OAuth client secrets
- Webhook signing secrets
- Third-party service credentials

**Anti-Patterns (Never Do This):**
```python
# ❌ Hardcoded in source code
DATABASE_PASSWORD = "super_secret_123"

# ❌ In version control
# .env file committed to Git
DB_PASSWORD=super_secret_123

# ❌ In container images
COPY secrets.json /app/

# ❌ In logs
logger.info(f"Connecting with password: {password}")

# ❌ In environment variables (visible in process list)
# Acceptable for non-critical, but not ideal for sensitive secrets
```

**Secure Patterns:**

**1. Centralized Secret Store:**
```python
# HashiCorp Vault example
import hvac

client = hvac.Client(url='https://vault.example.com', token=os.environ['VAULT_TOKEN'])

# Read secret
secret = client.secrets.kv.v2.read_secret_version(path='database/prod')
db_password = secret['data']['data']['password']

# Write secret (with access control)
client.secrets.kv.v2.create_or_update_secret(
    path='api/stripe',
    secret={'api_key': generate_random_key()}
)
```

**2. Cloud-Native Secret Management:**
```python
# AWS Secrets Manager
import boto3

client = boto3.client('secretsmanager')

# Retrieve secret
response = client.get_secret_value(SecretId='prod/database/password')
secret = json.loads(response['SecretString'])
db_password = secret['password']

# Rotate secret (automatic with Lambda function)
client.rotate_secret(
    SecretId='prod/database/password',
    RotationLambdaARN='arn:aws:lambda:us-east-1:123456789:function:rotate-db-creds'
)
```

**3. Kubernetes Secrets (with encryption at rest):**
```yaml
# External Secrets Operator - sync from Vault to K8s
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: database-credentials
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: vault-backend
    kind: SecretStore
  target:
    name: db-secret
    creationPolicy: Owner
  data:
  - secretKey: password
    remoteRef:
      key: database/prod
      property: password
---
# Pod consumes secret
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: app
    image: myapp:latest
    env:
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: password
```

**4. Secrets Rotation (Zero-Downtime):**
```python
class SecretRotation:
    def rotate_database_password(self):
        # Step 1: Generate new password
        new_password = generate_secure_password()

        # Step 2: Create new user with new password (dual-write)
        db_admin.create_user('app_user_v2', new_password)
        db_admin.grant_permissions('app_user_v2', same_as='app_user_v1')

        # Step 3: Update secret in Vault
        vault.write('database/password', {'version': 2, 'password': new_password})

        # Step 4: Rolling restart of app instances
        # (They fetch new secret on startup)
        kubernetes.rolling_restart('deployment/myapp')

        # Step 5: Wait for all instances to use new secret (monitor connections)
        wait_for_instances_updated()

        # Step 6: Revoke old user
        db_admin.drop_user('app_user_v1')

        # Step 7: Clean up old secret version
        vault.delete_version('database/password', version=1)
```

**5. Temporary Credentials (STS/IAM Roles):**
```python
# AWS: Use IAM roles instead of long-lived access keys
import boto3

# Application runs with IAM role attached (ECS task role, EC2 instance role)
# No credentials in code
s3 = boto3.client('s3')  # Automatically uses temporary credentials
s3.upload_file('file.txt', 'bucket-name', 'file.txt')

# Credentials rotate automatically every hour
```

**6. Secrets Scanning (Pre-Commit Hooks):**
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']

  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
```

**7. Secrets in CI/CD:**
```yaml
# GitHub Actions: Use encrypted secrets
name: Deploy
on: push
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to production
        env:
          API_KEY: ${{ secrets.PROD_API_KEY }}  # Encrypted, not in repo
        run: |
          deploy.sh --api-key "$API_KEY"
```

**8. Break-Glass Emergency Access:**
```python
# Envelope encryption: Encrypt data encryption key (DEK) with master key
# Master key split with Shamir's Secret Sharing (3 of 5 keyholders)

class BreakGlassAccess:
    def recover_secrets(self, share_1, share_2, share_3):
        # Require 3 physical keyholders present
        master_key = shamirs_secret_sharing.recover([share_1, share_2, share_3])

        # Log emergency access
        audit_log(
            event="break_glass_access",
            keyholders=[share_1.holder, share_2.holder, share_3.holder],
            severity="CRITICAL"
        )

        # Alert security team
        alert_security_team("Break-glass access activated")

        # Decrypt secrets
        encrypted_secrets = vault.get_encrypted_backup()
        secrets = decrypt_with_master_key(encrypted_secrets, master_key)

        # Time-limited access (4 hours)
        schedule_revocation(after_hours=4)

        return secrets
```

**Secrets Sprawl Detection:**
```bash
# Scan Git history for secrets
trufflehog git https://github.com/org/repo.git --json

# Scan container images
trivy image --scanners secret myapp:latest

# Scan configuration files
detect-secrets scan --all-files .

# Scan cloud resources
ScoutSuite --provider aws --report-dir ./report
```

**Comparison of Secret Stores:**

| Feature | Vault | AWS Secrets Manager | Azure Key Vault | GCP Secret Manager |
|---------|-------|---------------------|-----------------|-------------------|
| Encryption at rest | ✓ | ✓ | ✓ | ✓ |
| Automatic rotation | ✓ | ✓ (RDS, others) | ✓ | Manual |
| Versioning | ✓ | ✓ | ✓ | ✓ |
| Access policies | Fine-grained | IAM-based | RBAC | IAM-based |
| Audit logging | ✓ | CloudTrail | Activity Logs | Cloud Audit Logs |
| Multi-cloud | ✓ | AWS only | Azure only | GCP only |
| Dynamic secrets | ✓ | Limited | Limited | No |
| Cost | Self-hosted | $0.40/secret/month | $0.03/10k ops | $0.06/10k ops |

**Best Practices:**
- Never commit secrets to version control
- Use secret stores (Vault, cloud KMS)
- Rotate secrets regularly (90 days max for high-value)
- Use temporary credentials where possible (IAM roles, STS)
- Audit all secret access
- Encrypt secrets at rest and in transit
- Implement break-glass procedures
- Scan for secrets in code, images, logs
- Principle of least privilege for secret access

---

(Continuing in next message due to length...)

### XIV. Vulnerability Management
**Known vulnerabilities shall be remediated within risk-based SLAs.**

Continuous scanning of dependencies and infrastructure. Severity-based remediation timelines. Compensating controls when patches unavailable.

**Vulnerability Severity SLAs:**

| Severity | CVSS Score | Remediation SLA | Compensating Controls |
|----------|-----------|-----------------|----------------------|
| Critical | 9.0-10.0 | 24 hours | WAF rule, network isolation |
| High | 7.0-8.9 | 7 days | Monitoring, access restriction |
| Medium | 4.0-6.9 | 30 days | Risk acceptance with justification |
| Low | 0.1-3.9 | 90 days or next release | Backlog prioritization |

**Risk-Based Prioritization:**

CVSS score alone insufficient. Consider:
- **Exploitability**: EPSS (Exploit Prediction Scoring System) score
- **Exposure**: Internet-facing vs. internal
- **Data sensitivity**: PII, financial data, trade secrets
- **Business criticality**: Revenue-generating system vs. internal tool

**Prioritization Formula:**
```
Priority Score = CVSS × Exploitability × Exposure × Data_Sensitivity × Business_Impact

Example:
- Log4Shell: 10.0 × 0.95 (active exploitation) × 1.0 (internet-facing) × 1.0 (sensitive data) × 1.0 (critical) = 9.5 → CRITICAL
- Obscure library bug: 8.0 × 0.01 (no exploit) × 0.5 (internal) × 0.5 (non-sensitive) × 0.5 (non-critical) = 0.01 → LOW
```

**Vulnerability Scanning:**

**1. Dependency Scanning (SCA - Software Composition Analysis):**
```yaml
# GitHub Dependabot configuration
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    labels:
      - "dependencies"
      - "security"
    # Auto-merge patch updates for security
    auto-merge:
      - match:
          dependency-type: "direct"
          update-type: "security:patch"
```

**2. Container Image Scanning:**
```bash
# Scan Docker images for vulnerabilities
trivy image --severity HIGH,CRITICAL myapp:latest

# Fail CI/CD pipeline if critical vulns found
trivy image --exit-code 1 --severity CRITICAL myapp:latest
```

**3. Infrastructure Scanning:**
```bash
# Scan cloud infrastructure (AWS, Azure, GCP)
prowler aws --severity high

# Scan Kubernetes clusters
kube-bench run --targets node,policies

# Scan IaC templates
checkov --directory . --framework terraform
```

**4. Runtime Vulnerability Detection:**
```yaml
# Falco rules detect runtime anomalies
- rule: Unexpected outbound connection
  desc: Detect outbound connection to suspicious IP
  condition: outbound and not allowed_destinations
  output: "Suspicious connection (user=%user.name command=%proc.cmdline connection=%fd.name)"
  priority: WARNING
```

**Patch Management Process:**

**Phase 1: Discovery (Continuous)**
```
Automated scanners run daily → Vulnerabilities detected → Tickets created → Triaged by severity
```

**Phase 2: Assessment (Within 24-48 hours)**
```
Security team reviews → Determines exploitability → Assigns priority → Notifies affected teams
```

**Phase 3: Remediation (Per SLA)**
```
Critical: Hotfix deployed immediately → Tested in staging → Deployed to production
High: Scheduled for next sprint → Tested → Deployed
Medium/Low: Backlog → Normal release cycle
```

**Phase 4: Verification**
```
Re-scan after patching → Verify vulnerability resolved → Close ticket → Update metrics
```

**Compensating Controls (When Immediate Patching Impossible):**

**1. Virtual Patching (WAF Rules):**
```
Vulnerability: SQL injection in legacy app (cannot patch immediately)
Compensating control: WAF rule blocks SQLi patterns
Duration: Until app can be patched (max 30 days)
```

**2. Network Isolation:**
```
Vulnerability: RCE in internal service
Compensating control: Restrict network access via firewall rules (only allow known IPs)
```

**3. Runtime Protection (RASP):**
```
Vulnerability: Deserialization flaw
Compensating control: Runtime application self-protection blocks malicious payloads
```

**4. Enhanced Monitoring:**
```
Vulnerability: Authentication bypass (patch in progress)
Compensating control: Alert on any authentication failures + IP blocking
```

**Vulnerability Disclosure Program:**

**Bug Bounty:**
```yaml
# HackerOne program configuration
program:
  name: MyCompany Security
  scope:
    in_scope:
      - *.example.com (excluding test.example.com)
      - mobile apps (iOS, Android)
    out_of_scope:
      - test.example.com
      - third-party services
  rewards:
    critical: $5,000 - $20,000
    high: $1,000 - $5,000
    medium: $250 - $1,000
    low: $50 - $250
  response_sla:
    first_response: 24 hours
    triage: 48 hours
    resolution: severity-based (per table above)
```

**Coordinated Disclosure Process:**
```
1. Researcher reports vulnerability → Security team acknowledges (24h)
2. Triage and validate (48h) → Determine severity
3. Develop fix → Test in staging
4. Deploy fix to production
5. Public disclosure (90 days after report or after fix, whichever is sooner)
6. Reward researcher → CVE assignment if applicable
```

**Metrics:**

- **Mean Time To Remediate (MTTR)**: Average time from vulnerability discovery to fix
- **Vulnerability density**: Vulns per 1000 lines of code
- **SLA compliance**: % of vulnerabilities fixed within SLA
- **Vulnerability age**: Distribution of open vulnerabilities by age
- **Coverage**: % of assets scanned regularly

**Example Dashboard:**
```
Current Vulnerabilities:
  Critical: 2 (both < 12 hours old) ✓
  High: 15 (avg age: 4 days) ✓
  Medium: 87 (avg age: 18 days) ✓
  Low: 203 (avg age: 45 days) ⚠️

SLA Compliance: 94%
MTTR: 5.2 days (target: < 7 days)
Scan Coverage: 98% of production assets
```

**Zero-Day Response:**

**Phase 1: Detection (0-4 hours)**
- Threat intelligence feeds alert on new zero-day
- Security team convenes emergency meeting
- Assess impact on organization

**Phase 2: Containment (4-12 hours)**
- Implement compensating controls (WAF rules, network isolation)
- Disable affected features if necessary
- Alert customers if SaaS provider

**Phase 3: Remediation (12-72 hours)**
- Deploy vendor patch if available
- Develop custom patch if vendor slow
- Test thoroughly before production deployment

**Phase 4: Recovery (72+ hours)**
- Remove compensating controls after verification
- Conduct post-incident review
- Update playbooks

---

### XV. Immutable Infrastructure & Reproducible Builds
**Production systems built from version-controlled definitions; compromise requires redeployment, not persistence.**

Infrastructure as code. Immutable images. No SSH to production for modifications. Compromised instances replaced, not repaired.

**Principles:**

**1. Infrastructure as Code (IaC):**

All infrastructure defined in version-controlled files:
```hcl
# Terraform example
resource "aws_instance" "web" {
  ami           = data.aws_ami.app_image.id  # Immutable AMI
  instance_type = "t3.medium"

  # No SSH access
  key_name = null

  # Managed by auto-scaling, not manual intervention
  lifecycle {
    create_before_destroy = true
    ignore_changes = []  # Any manual changes cause drift
  }

  tags = {
    Name        = "web-server"
    Environment = "production"
    ManagedBy   = "terraform"
  }
}
```

**2. Immutable Container Images:**

**Build Process:**
```dockerfile
# Multi-stage build for minimal attack surface
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

FROM node:18-alpine
RUN apk add --no-cache dumb-init
USER node
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules

# Read-only filesystem (immutable)
# No shells, no package managers in final image

ENTRYPOINT ["dumb-init", "node", "dist/server.js"]
```

**Image Signing and Verification:**
```bash
# Sign image with Cosign (Sigstore)
cosign sign --key cosign.key myregistry.io/myapp:v1.2.3

# Deploy only signed images (Kubernetes admission controller)
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: require-signed-images
spec:
  images:
  - glob: "myregistry.io/*"
  authorities:
  - key:
      data: |
        -----BEGIN PUBLIC KEY-----
        ...
        -----END PUBLIC KEY-----
```

**3. GitOps Deployment:**

```yaml
# ArgoCD application definition
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/myapp-manifests
    targetRevision: main
    path: k8s
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true  # Remove resources not in Git
      selfHeal: true  # Revert manual changes
```

**Benefits:**
- All changes go through Git (code review, audit trail)
- Drift detection: manual changes automatically reverted
- Rollback: `git revert` + automatic redeployment

**4. No SSH Access to Production:**

**Traditional (Bad):**
```bash
# SSH into server to debug
ssh ubuntu@prod-server-1
# Make manual changes
sudo vim /etc/nginx/nginx.conf
sudo systemctl restart nginx
# Changes undocumented, can't be reproduced
```

**Immutable (Good):**
```bash
# Debug via read-only logs/metrics
kubectl logs myapp-pod-abc123
kubectl exec -it myapp-pod-abc123 -- sh  # Read-only, no write permissions

# Changes go through Git
vim terraform/main.tf  # Update infrastructure definition
git commit -m "Update nginx config"
git push  # Triggers automated deployment
```

**Break-Glass Access (Emergencies Only):**
```python
# Temporary SSH access for incident response
class BreakGlassAccess:
    def grant_ssh_access(self, instance_id, engineer, duration_hours=4):
        # Require manager + security approval
        approval = require_approval([engineer.manager, security_team])

        # Generate temporary SSH key
        ssh_key = generate_temporary_key(ttl=duration_hours)

        # Add to instance
        ec2.add_ssh_key(instance_id, ssh_key.public_key)

        # Schedule automatic revocation
        schedule_revocation(instance_id, ssh_key, after=duration_hours)

        # Log all commands executed
        enable_session_recording(instance_id, engineer)

        # Alert security team
        alert(f"Break-glass SSH access granted to {engineer} for {instance_id}")
```

**5. Configuration Drift Detection:**

```bash
# Detect manual changes to infrastructure
terraform plan -detailed-exitcode
# Exit code 2 = drift detected

# Alert on drift
if [ $? -eq 2 ]; then
    echo "Configuration drift detected!"
    terraform show  # Show differences
    notify_team "Manual changes detected in production"
    # Option 1: Auto-remediate
    terraform apply -auto-approve
    # Option 2: Require manual review
fi
```

**6. Reproducible Builds:**

**Goal**: Same source code → same binary output (byte-for-byte identical)

**Benefits:**
- Verify build integrity (no supply chain tampering)
- Independent verification by third parties

**Example:**
```dockerfile
# Use specific base image hash (not :latest tag)
FROM node:18.12.0@sha256:3c9e...

# Pin all dependencies
COPY package-lock.json ./  # Exact versions

# Set deterministic timestamps
RUN find /app -exec touch -t 202501010000 {} +

# Remove build metadata
RUN rm -rf /root/.npm /tmp/*
```

**Verification:**
```bash
# Build twice, compare hashes
docker build -t myapp:v1 .
sha256sum myapp_v1.tar > hash1.txt

docker build -t myapp:v1 .  # Build again
sha256sum myapp_v1.tar > hash2.txt

diff hash1.txt hash2.txt  # Should be identical
```

**7. Incident Response for Compromised Systems:**

**Traditional Approach (Manual Repair):**
```
1. SSH into compromised server
2. Kill malicious processes
3. Remove malware
4. Patch vulnerabilities
5. Hope attacker didn't leave backdoor
```
**Problem**: Attacker may have persistence mechanisms, rootkits, modified binaries.

**Immutable Approach (Replace, Not Repair):**
```
1. Isolate compromised instance (network segmentation)
2. Capture memory dump + disk snapshot (forensics)
3. Terminate instance
4. Deploy fresh instance from known-good image
5. Investigate snapshot offline
6. Identify root cause → fix vulnerability → redeploy
```

**8. Stateless Applications:**

```
Application state stored externally (database, Redis, S3)
  ↓
Instances can be replaced anytime without data loss
  ↓
Auto-scaling, rolling deployments, blue-green deploys trivial
```

**Example:**
```python
# Bad: Store session in local memory
sessions = {}  # Lost if instance terminates

# Good: Store session in Redis
import redis
session_store = redis.Redis(host='redis.example.com')
```

**9. Supply Chain Security (Image Provenance):**

```yaml
# SLSA (Supply-chain Levels for Software Artifacts) compliance
# Generate provenance attestation
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: build-with-provenance
spec:
  steps:
  - name: build
    image: gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/git-init:latest
    script: |
      docker build -t myapp:${VERSION} .
      # Generate provenance
      slsa-github-generator generate \
        --artifact myapp:${VERSION} \
        --source-repo github.com/myorg/myapp \
        --source-sha ${COMMIT_SHA}
```

**Verification:**
```bash
# Verify image provenance before deployment
slsa-verifier verify-image myapp:v1.2.3 \
  --source-uri github.com/myorg/myapp \
  --source-tag v1.2.3
```

**Trade-offs:**

| Aspect | Immutable | Mutable | Notes |
|--------|-----------|---------|-------|
| Security | High (replace, not patch) | Medium (manual patching) | Immutable prevents persistence |
| Debugging | Harder (no SSH) | Easier (can modify live) | Use observability instead of SSH |
| Deployment speed | Slower (rebuild image) | Faster (patch in place) | Cache layers to speed up |
| Consistency | High (all instances identical) | Low (drift over time) | Immutable = deterministic |

---

### XVI. Threat Modeling
**Security design begins with systematic threat identification; STRIDE, attack trees, and abuse cases inform architecture.**

Threat modeling in design phase, not post-implementation. Identify threats before writing code. Mitigations integrated into architecture.

**When to Threat Model:**

- New features/products (before implementation)
- Architecture changes (refactoring, cloud migration)
- Security incidents (post-mortem, prevent recurrence)
- Regular reviews (annually for critical systems)

**Threat Modeling Methodologies:**

**1. STRIDE (Microsoft):**

| Threat | Security Property Violated | Example | Mitigation |
|--------|---------------------------|---------|------------|
| **S**poofing | Authentication | Attacker impersonates user | MFA, certificates |
| **T**ampering | Integrity | Modify data in transit | HMAC, digital signatures |
| **R**epudiation | Non-repudiation | Deny performing action | Audit logs, signatures |
| **I**nformation Disclosure | Confidentiality | Leak sensitive data | Encryption, access controls |
| **D**enial of Service | Availability | Exhaust resources | Rate limiting, auto-scaling |
| **E**levation of Privilege | Authorization | Gain unauthorized access | Least privilege, RBAC |

**2. PASTA (Process for Attack Simulation and Threat Analysis):**

7-stage process:
1. Define business objectives
2. Define technical scope
3. Application decomposition
4. Threat analysis
5. Vulnerability analysis
6. Attack modeling
7. Risk/impact analysis

**3. Attack Trees:**

```
Goal: Steal Customer Credit Cards
├─ [OR] Compromise Database
│   ├─ [AND] SQL Injection
│   │   ├─ Find vulnerable input field
│   │   └─ Extract data via UNION queries
│   ├─ [AND] Stolen DB Credentials
│   │   ├─ Phish DBA
│   │   └─ Login from external IP
│   └─ [AND] Insider Threat
│       └─ Bribe employee
├─ [OR] Man-in-the-Middle
│   ├─ [AND] Intercept HTTPS Traffic
│   │   ├─ Compromise CA
│   │   └─ Issue fake certificate
│   └─ [AND] Network Sniffing
│       └─ Access internal network
└─ [OR] Client-Side Attack
    ├─ XSS to steal card data from form
    └─ Malicious browser extension
```

**Threat Modeling Process:**

**Step 1: Create Data Flow Diagram (DFD)**

```
[User] --1--> [Web Browser] --2--> [Load Balancer] --3--> [App Server] --4--> [Database]
                                                                              ↓
                                                                        [Audit Logs]

Trust Boundaries:
- Between User and Web Browser (untrusted network)
- Between Load Balancer and App Server (DMZ → internal network)
- Between App Server and Database (application → data tier)
```

**Step 2: Identify Threats (STRIDE per element)**

```
[Web Browser]
  - Spoofing: Phishing site impersonates legitimate app
  - Information Disclosure: XSS leaks session token
  - Tampering: MITM modifies requests

[Load Balancer]
  - DoS: Flood with requests
  - Elevation of Privilege: Exploit LB vulnerability to access backend

[App Server]
  - Injection: SQL injection, command injection
  - Authentication bypass
  - Tampering: Modify source code

[Database]
  - Information Disclosure: SQL injection dumps data
  - Elevation of Privilege: Privilege escalation to DBA
  - Tampering: Modify financial records
```

**Step 3: Determine Mitigations**

| Threat | Mitigation | Priority | Status |
|--------|------------|----------|--------|
| XSS in web app | CSP headers, output encoding | HIGH | ✓ Implemented |
| SQL injection | Parameterized queries, ORM | HIGH | ✓ Implemented |
| MITM attack | HTTPS with HSTS, cert pinning | HIGH | ✓ Implemented |
| Credential stuffing | Rate limiting, CAPTCHA, MFA | MEDIUM | ⚠️ Planned |
| DDoS | CDN, WAF, auto-scaling | MEDIUM | ✓ Implemented |
| Session hijacking | Secure cookies, short expiry | HIGH | ✓ Implemented |
| Privilege escalation | Least privilege, RBAC | HIGH | ✓ Implemented |

**Step 4: Validate Mitigations**

```python
# Security test cases derived from threat model
def test_xss_prevention():
    # Threat: XSS via user input
    # Mitigation: Output encoding
    malicious_input = "<script>alert('XSS')</script>"
    response = app.render_profile(username=malicious_input)
    assert "<script>" not in response
    assert "&lt;script&gt;" in response  # Properly encoded

def test_sql_injection_prevention():
    # Threat: SQL injection
    # Mitigation: Parameterized queries
    malicious_input = "admin' OR '1'='1"
    user = db.get_user(username=malicious_input)
    assert user is None  # Should not return any user

def test_rate_limiting():
    # Threat: Brute force authentication
    # Mitigation: Rate limiting
    for i in range(10):
        response = app.login("user", "wrong_password")
    response = app.login("user", "any_password")
    assert response.status_code == 429  # Too Many Requests
```

**4. Abuse Cases (Complement Use Cases):**

```
Use Case: User resets forgotten password
  → Email sent with reset link
  → User clicks link, sets new password

Abuse Cases:
1. Attacker requests password reset for victim's email
   → Mitigation: Reset link sent to registered email only, requires email access
2. Attacker intercepts reset link from email
   → Mitigation: HTTPS, short expiry (15 min), single-use token
3. Attacker brute-forces reset token
   → Mitigation: Cryptographically secure token (128+ bits), rate limiting
4. Attacker reuses old reset link
   → Mitigation: Tokens invalidated after use or expiry
5. Attacker requests password resets to DoS user
   → Mitigation: Rate limit reset requests (3 per hour per email)
```

**5. LINDDUN (Privacy Threat Modeling):**

For GDPR/privacy compliance:

| Threat | Example | Mitigation |
|--------|---------|------------|
| **L**inking | Correlate user across datasets | Pseudonymization, separate DBs |
| **I**dentifying | De-anonymize user | k-anonymity, differential privacy |
| **N**on-repudiation | User can't deny action | Allow plausible deniability where appropriate |
| **D**etectability | Infer sensitive attributes | Data minimization |
| **D**isclosure | Leak PII | Encryption, access controls |
| **U**nawareness | Users unaware of data collection | Privacy policy, consent UX |
| **N**on-compliance | Violate GDPR | DPO, DPIA, retention policies |

**Threat Model as Living Document:**

```
Documentation:
  - Store in version control (Git)
  - Update with every feature/architecture change
  - Review annually (minimum)
  - Reference in security reviews

Format:
  - Data flow diagrams (draw.io, Lucidchart)
  - Threat matrix (Markdown, spreadsheet)
  - Mitigation tracking (Jira, GitHub Issues)

Integration:
  - Link to design docs
  - Reference in code reviews
  - Security testing mapped to threats
  - Incident post-mortems update threat model
```

**Example Threat Model Template:**

```markdown
# Threat Model: Payment Processing Feature

## Overview
Feature allows users to purchase products with credit cards.

## Assets
- Customer credit card data (PCI-DSS)
- Payment history
- User accounts

## Trust Boundaries
1. User browser ↔ Application (public internet)
2. Application ↔ Payment gateway (API)
3. Application ↔ Database (internal network)

## Threats (STRIDE)

### Payment Form (Browser)
| ID | Threat | Type | Severity | Mitigation | Status |
|----|--------|------|----------|------------|--------|
| T1 | XSS steals card data from form | I | Critical | CSP, output encoding | Done |
| T2 | MITM intercepts card submission | I | Critical | HTTPS, HSTS, no HTTP | Done |
| T3 | Malicious browser extension | I | Medium | User education | N/A |

### Application Server
| ID | Threat | Type | Severity | Mitigation | Status |
|----|--------|------|----------|------------|--------|
| T4 | Logs contain full card numbers | I | Critical | Redact logs (PCI requirement) | Done |
| T5 | Payment amount tampering | T | High | Server-side validation | Done |
| T6 | Replay attack (reuse payment) | T | High | Idempotency keys | Done |

### Database
| ID | Threat | Type | Severity | Mitigation | Status |
|----|--------|------|----------|------------|--------|
| T7 | Unauthorized access to card data | E, I | Critical | Tokenization (no cards stored) | Done |
| T8 | Backup files leaked | I | Critical | Encrypted backups | Done |

## Assumptions
- Payment gateway (Stripe) is trusted
- TLS certificates properly validated
- Database encrypted at rest

## Out of Scope
- Physical security of data center
- Payment gateway security (third-party)
- Social engineering attacks on users

## Review History
- 2025-11-20: Initial threat model (v1.0)
- Next review: 2026-05-20 (6 months)
```

**Tools:**

- **Microsoft Threat Modeling Tool**: Free, STRIDE-based
- **OWASP Threat Dragon**: Open source, web-based
- **IriusRisk**: Commercial, automated
- **ThreatModeler**: Commercial, collaboration features
- **draw.io / Lucidchart**: DFD creation

**Benefits:**

- Find security flaws early (cheaper to fix)
- Systematic coverage (not ad-hoc)
- Documentation for new team members
- Compliance requirement (PCI-DSS, ISO 27001)
- Security test case generation

---

### XVII. Supply Chain Security
**Dependencies are attack vectors; verify provenance, pin versions, scan continuously, minimize third-party code.**

Modern applications built from hundreds of dependencies. Each is a potential attack vector. SolarWinds, Log4Shell, event-stream malware demonstrate supply chain risks.

**Supply Chain Attack Vectors:**

1. **Compromised dependencies**: Malicious code in packages (NPM, PyPI, Maven)
2. **Dependency confusion**: Attacker uploads package with same name to public registry
3. **Typosquatting**: Malicious package with similar name (`react-dom` vs. `reactdom`)
4. **Account takeover**: Attacker compromises maintainer account
5. **Build system compromise**: CI/CD pipeline injected with malware
6. **Compromised update mechanism**: Malicious auto-updates

**Mitigation Strategies:**

**1. Software Bill of Materials (SBOM):**

Generate and verify SBOM for all software:

```bash
# Generate SBOM using Syft
syft packages myapp:latest -o spdx-json > sbom.json

# Verify SBOM integrity
cosign verify --key cosign.pub sbom.json
```

**SBOM Contents:**
- All direct and transitive dependencies
- Dependency versions
- Licenses
- Known vulnerabilities (CVEs)

**2. Dependency Pinning:**

```json
// BAD: Unpinned dependencies (package.json)
{
  "dependencies": {
    "express": "^4.0.0",  // Will auto-update to 4.x.x
    "lodash": "*"          // Will update to any version
  }
}

// GOOD: Pinned dependencies (package-lock.json)
{
  "dependencies": {
    "express": {
      "version": "4.18.2",  // Exact version
      "resolved": "https://registry.npmjs.org/express/-/express-4.18.2.tgz",
      "integrity": "sha512-...",  // Verify hash
    }
  }
}
```

**Lock files:**
- NPM: `package-lock.json`
- Python: `requirements.txt` with `pip freeze`, or `poetry.lock`
- Go: `go.sum`
- Rust: `Cargo.lock`
- Maven: `maven.lock` or explicit versions in `pom.xml`

**3. Package Signature Verification:**

```bash
# NPM: Verify package signatures
npm config set audit-level moderate
npm audit signatures  # Verify registry signatures

# Python: Use pip with hash verification
pip install --require-hashes -r requirements.txt

# requirements.txt with hashes
requests==2.28.1 \
    --hash=sha256:8fefa2a1a1365bf5520aac41836fbee479da67864514bdb821f31ce07ce65349
```

**4. Private Package Registry/Mirror:**

```yaml
# .npmrc - Use private registry
registry=https://npm.internal.example.com

# Verdaccio (private NPM proxy)
# Benefits:
# - Cache packages (resilience)
# - Scan before allowing
# - Prevent dependency confusion
# - Audit all package downloads
```

**5. Dependency Confusion Prevention:**

```
Attack: Attacker publishes malicious package to public registry
        with same name as internal package

Example:
  Internal package: @mycompany/auth (private registry)
  Attacker publishes: @mycompany/auth (npmjs.com, higher version)
  NPM installs attacker package instead of internal

Prevention:
  1. Use package scopes (@mycompany/*) with private registry
  2. Configure registry precedence
  3. Monitor for namespace squatting
```

**NPM Configuration:**
```bash
# Always use private registry for scoped packages
@mycompany:registry=https://npm.internal.example.com
```

**6. Automated Dependency Scanning:**

```yaml
# Continuous dependency scanning (GitHub Actions)
name: Dependency Scan
on:
  schedule:
    - cron: '0 0 * * *'  # Daily
  pull_request:

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run Snyk
        run: |
          npm install -g snyk
          snyk test --severity-threshold=high
          snyk monitor  # Continuous monitoring

      - name: Run OWASP Dependency-Check
        run: |
          dependency-check --project myapp \
            --scan . \
            --format JSON \
            --failOnCVSS 7

      - name: Run Trivy
        run: |
          trivy fs . --severity HIGH,CRITICAL
```

**7. Vet New Dependencies:**

Before adding dependency, review:
```
Checklist:
  [ ] Actively maintained? (commits in last 3 months)
  [ ] Reputable maintainers? (GitHub profile, contributions)
  [ ] Number of downloads? (popular = more eyeballs)
  [ ] Open issues/PRs response time? (maintained)
  [ ] License compatible? (MIT, Apache 2.0, etc.)
  [ ] Known vulnerabilities? (CVE database)
  [ ] Code quality? (brief code review)
  [ ] Minimal dependencies? (less transitive risk)
  [ ] Alternative solutions? (use standard library if possible)
```

**Example Tool:**
```bash
# OSS Review Toolkit (ORT)
ort analyze -i . -o results/
ort scan -i results/analyzer-result.yml -o results/
ort report -f StaticHtml -i results/scan-result.yml -o report/
```

**8. Monitor for Malicious Updates:**

```yaml
# Renovate bot configuration
{
  "extends": ["config:base"],
  "dependencyDashboard": true,
  "prCreation": "not-pending",
  "automerge": false,  # Never auto-merge, always review

  "packageRules": [
    {
      "matchUpdateTypes": ["major"],
      "automerge": false,  # Major updates require manual review
      "labels": ["security-review"]
    },
    {
      "matchDepTypes": ["dependencies"],
      "matchUpdateTypes": ["patch"],
      "automerge": true,  # Auto-merge security patches
      "automergeType": "pr",
      "automergeStrategy": "squash",
      "schedule": ["before 5am"]
    }
  ]
}
```

**9. Build Provenance (SLSA Framework):**

**SLSA Level 1**: Documentation of build process
**SLSA Level 2**: Tamper-proof build service (CI/CD)
**SLSA Level 3**: Verifiable provenance
**SLSA Level 4**: Two-party review + hermetic builds

```yaml
# GitHub Actions with provenance generation
name: Build with Provenance
on: push

jobs:
  build:
    permissions:
      id-token: write  # For SLSA provenance
      contents: read

    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Build
        run: |
          docker build -t myapp:${{ github.sha }} .

      - name: Generate provenance
        uses: slsa-framework/slsa-github-generator@v1.9.0
        with:
          artifact: myapp:${{ github.sha }}
```

**Verification:**
```bash
# Verify artifact provenance
slsa-verifier verify-image myapp:abc123 \
  --source-uri github.com/myorg/myapp \
  --source-tag v1.2.3 \
  --print-provenance
```

**10. Vendor Security Assessments:**

For third-party SaaS dependencies:
```
Vendor Security Questionnaire:
  [ ] SOC 2 Type II certified?
  [ ] Penetration testing frequency?
  [ ] Incident response plan?
  [ ] Data encryption (at rest, in transit)?
  [ ] Employee background checks?
  [ ] Access controls (RBAC, MFA)?
  [ ] Vulnerability disclosure program?
  [ ] Business continuity plan?
  [ ] Data retention and deletion policies?
  [ ] Compliance certifications (ISO 27001, HIPAA)?
  [ ] Subprocessors disclosed?
```

**11. Code Signing:**

```bash
# Sign all releases
gpg --detach-sign --armor myapp-v1.2.3.tar.gz

# Users verify signature before running
gpg --verify myapp-v1.2.3.tar.gz.asc myapp-v1.2.3.tar.gz
```

**For containers:**
```bash
# Sign Docker images
cosign sign --key cosign.key myregistry.io/myapp:v1.2.3

# Admission controller rejects unsigned images
kubectl apply -f policy-controller-config.yaml
```

**12. Supply Chain Security Tools:**

| Tool | Purpose | Open Source |
|------|---------|-------------|
| Dependabot | Automated dependency updates | ✓ (GitHub) |
| Renovate | Dependency updates | ✓ |
| Snyk | Vulnerability scanning | Freemium |
| OWASP Dependency-Check | SCA | ✓ |
| Trivy | Container/filesystem scanning | ✓ |
| Syft | SBOM generation | ✓ |
| Cosign | Artifact signing | ✓ |
| SLSA Provenance | Build attestation | ✓ |
| OSS Review Toolkit (ORT) | License/security compliance | ✓ |
| Grafeas | Artifact metadata | ✓ |
| in-toto | Supply chain integrity | ✓ |

**Real-World Examples:**

**SolarWinds (2020):**
- Build system compromised
- Malicious code injected into software updates
- Affected 18,000 organizations
- Lesson: Verify build integrity, SLSA provenance

**Log4Shell (2021):**
- Zero-day in Log4j library
- Transitive dependency in many applications
- CVSS 10.0 (critical)
- Lesson: Dependency scanning, SBOM for visibility

**event-stream NPM (2018):**
- Maintainer transferred ownership
- New maintainer injected cryptocurrency stealer
- Lesson: Monitor dependency maintainer changes

**ua-parser-js NPM (2021):**
- Maintainer account compromised
- Malicious versions published
- Lesson: 2FA for maintainer accounts, package signing

---

### XVIII. Security Monitoring & Incident Response
**Assume breach; detect intrusions rapidly; respond with playbooks; conduct blameless post-mortems.**

Security monitoring and incident response are continuous processes. Assume attackers are already in your environment; detect and respond quickly.

**Detection Capabilities:**

**1. Security Information and Event Management (SIEM):**

Centralized log aggregation, correlation, and alerting.

**SIEM Architecture:**
```
[Applications, Servers, Network Devices, Cloud Services]
                    ↓
        [Log Collectors/Shippers]
         (Filebeat, Fluentd, CloudWatch)
                    ↓
        [Log Aggregation Pipeline]
               (Kafka, Kinesis)
                    ↓
            [SIEM Platform]
     (Splunk, ELK, Datadog, Sumo Logic)
                    ↓
    [Correlation Rules, ML Anomaly Detection]
                    ↓
    [Alerts → Security Operations Center (SOC)]
```

**2. Security Orchestration, Automation, and Response (SOAR):**

Automate incident response workflows.

**Example Playbook:**
```yaml
# Playbook: Suspected compromised user account
trigger:
  - High-risk login (impossible travel, new device, failed MFA)

actions:
  - step: 1
    action: Enrich context
    tasks:
      - Query user activity in last 24h
      - Get device fingerprint
      - Check against threat intelligence feeds

  - step: 2
    action: Containment
    tasks:
      - Disable user account (temporary)
      - Terminate active sessions
      - Block IP address (if malicious)

  - step: 3
    action: Notify
    tasks:
      - Alert user via out-of-band channel (SMS)
      - Create incident ticket
      - Notify security team (Slack/PagerDuty)

  - step: 4
    action: Investigate
    tasks:
      - Review login attempts
      - Check for data exfiltration
      - Analyze network traffic

  - step: 5
    action: Remediate
    tasks:
      - Force password reset (if confirmed compromise)
      - Re-enable account after user verification
      - Update threat intelligence

  - step: 6
    action: Document
    tasks:
      - Incident report
      - Lessons learned
      - Update playbook
```

**3. Detection Rules:**

**Anomaly Detection (ML-based):**
```python
# Detect unusual database queries (volume)
baseline = calculate_baseline(user_id, metric='queries_per_hour', window='30 days')
current = get_current_metric(user_id, 'queries_per_hour')

if current > baseline.mean + (3 * baseline.std_dev):  # Z-score > 3
    alert(f"Anomalous query volume for user {user_id}: {current} (baseline: {baseline.mean})")
```

**Signature-Based Detection:**
```yaml
# Detect SQL injection attempts
rule: sql_injection_attempt
source: application_logs
pattern: |
  error.message CONTAINS "SQL syntax" OR
  request.query_params CONTAINS "UNION SELECT" OR
  request.query_params CONTAINS "' OR '1'='1"
severity: HIGH
action:
  - alert: security-team@example.com
  - block_ip: true
  - duration: 1 hour
```

**Behavior-Based Detection:**
```python
# Detect credential stuffing attack
login_attempts = get_login_attempts(ip_address, window='5 minutes')

unique_usernames = set(attempt.username for attempt in login_attempts)

if len(unique_usernames) > 20:  # Many different usernames from same IP
    alert(f"Credential stuffing from {ip_address}: {len(unique_usernames)} usernames")
    block_ip(ip_address, duration='1 hour')
```

**4. Indicators of Compromise (IoCs):**

Monitor for known attack patterns:

```yaml
# IoC feed integration
iocs:
  - type: ip_address
    value: 203.0.113.42
    threat: APT28 C2 server
    source: CISA

  - type: file_hash
    value: sha256:abc123...
    threat: Emotet malware
    source: VirusTotal

  - type: domain
    value: malicious-phishing-site.com
    threat: Phishing campaign
    source: PhishTank

# Alert if any IoC matched
rule: ioc_match
trigger: network_traffic.dest_ip IN ioc_list.ip_addresses
action: alert + block + investigate
```

**5. Threat Intelligence:**

```python
# Enrich alerts with threat intelligence
def enrich_alert(ip_address):
    # Query threat intel feeds
    virustotal_score = virustotal.get_score(ip_address)
    abuseipdb_reports = abuseipdb.get_reports(ip_address)
    shodan_info = shodan.get_info(ip_address)

    return {
        'ip': ip_address,
        'virustotal_malicious_count': virustotal_score,
        'abuseipdb_confidence': abuseipdb_reports['confidence'],
        'shodan_open_ports': shodan_info['ports'],
        'reputation': calculate_reputation(virustotal_score, abuseipdb_reports)
    }
```

**Incident Response Phases:**

**1. Preparation:**
- Incident response plan documented
- IR team identified and trained
- Tools configured (SIEM, SOAR, forensics)
- Playbooks tested (tabletop exercises)
- Communication channels established

**2. Detection:**
- SIEM alerts
- User reports
- Threat intelligence
- Vulnerability scans

**3. Containment:**

**Short-term containment:**
- Isolate compromised systems (network segmentation)
- Disable compromised accounts
- Block malicious IPs
- Patch vulnerabilities

**Long-term containment:**
- Deploy compensating controls
- Monitor attacker activity (deception technology)
- Prepare for eradication

**4. Eradication:**
- Remove malware
- Close attack vectors
- Patch vulnerabilities
- Rebuild compromised systems from clean images

**5. Recovery:**
- Restore from backups (verified clean)
- Bring systems back online
- Monitor for reinfection
- Gradual return to normal operations

**6. Lessons Learned (Post-Mortem):**
- Root cause analysis
- Timeline reconstruction
- What went well, what didn't
- Action items to prevent recurrence
- Update playbooks and detection rules

**Incident Severity Classification:**

| Severity | Criteria | Response Time | Escalation |
|----------|---------|---------------|------------|
| **P0 - Critical** | Data breach, ransomware, production outage | 15 minutes | Incident Commander, CISO, CEO |
| **P1 - High** | Confirmed compromise, active attack | 1 hour | Security team lead, Director |
| **P2 - Medium** | Suspicious activity, potential compromise | 4 hours | On-call security engineer |
| **P3 - Low** | Policy violation, informational alert | 1 business day | Queue for review |

**Incident Response Playbook Template:**

```markdown
# Incident Playbook: Ransomware

## Scope
Ransomware detected on endpoints or servers.

## Indicators
- File encryption activity (many files renamed with .encrypted)
- Ransom notes (README.txt, HOW_TO_DECRYPT.txt)
- Unusual process execution (crypto.exe, locker.exe)
- Network traffic to known ransomware C2 servers

## Immediate Actions (15 minutes)
1. Isolate affected systems (disconnect from network)
2. Preserve evidence (disk image, memory dump)
3. Identify ransomware variant (ransom note, file extensions)
4. Check for decryption tools (NoMoreRansom.org)

## Containment (1 hour)
5. Isolate network segments (prevent lateral movement)
6. Disable user accounts (if credentials compromised)
7. Block C2 domains/IPs at firewall
8. Identify entry point (phishing email, RDP brute force)

## Eradication (4-24 hours)
9. Remove ransomware (antivirus, manual removal)
10. Patch vulnerabilities (RDP, SMB, etc.)
11. Reset compromised credentials
12. Rebuild infected systems from clean images

## Recovery (24-72 hours)
13. Restore data from backups (verify clean)
14. Test restored systems
15. Bring systems back online gradually
16. Monitor for reinfection (7 days)

## Communication
- Internal: Incident Commander → Leadership (immediately)
- External: Legal team determines if breach notification required (GDPR, state laws)
- Law enforcement: FBI, local authorities (if advised by legal)
- Cyber insurance: File claim

## Post-Incident
- Root cause analysis
- Improve backups (offline, immutable)
- Security awareness training (anti-phishing)
- Update detection rules
- Tabletop exercise to test playbook

## Contacts
- Incident Commander: security-lead@example.com, +1-555-0100
- CISO: ciso@example.com, +1-555-0101
- Legal: legal@example.com, +1-555-0102
- Cyber Insurance: policy-123@insurer.com, +1-555-0103
```

**Metrics (SOC Performance):**

- **Mean Time To Detect (MTTD)**: Average time from compromise to detection
- **Mean Time To Respond (MTTR)**: Average time from detection to containment
- **False Positive Rate**: % of alerts that are false alarms
- **Alert Volume**: Number of alerts per day (trend)
- **Incident Volume**: Number of confirmed incidents (trend)
- **Dwell Time**: Time attacker remains undetected in environment

**Target Metrics:**
```
MTTD: < 1 hour (goal: minutes)
MTTR: < 4 hours
False Positive Rate: < 10%
Incident Closure Time: < 24 hours (P3), < 1 hour (P0)
```

**Tabletop Exercises:**

Regular practice scenarios:
```
Scenario 1: Phishing email with malware attachment
  - Some users click and download malware
  - How to detect? Contain? Eradicate?

Scenario 2: Insider threat exfiltrates data
  - Employee downloads customer database to USB
  - Detection mechanisms? Response?

Scenario 3: DDoS attack takes down website
  - Mitigation? Communication? Recovery?

Scenario 4: Zero-day vulnerability disclosed
  - Vulnerability in widely-used library
  - Patching process? Compensating controls?

Schedule: Quarterly (at minimum)
Participants: Security team, IT, legal, communications, leadership
Duration: 2-3 hours
Output: Action items, updated playbooks
```

**Communication Plan:**

**Internal:**
```
Incident Declared (P0)
  ↓
Incident Commander notifies CISO (immediate)
  ↓
CISO notifies CEO, Board (if material)
  ↓
Regular status updates (every 2 hours during active incident)
  ↓
All-clear declared → post-mortem scheduled (within 1 week)
```

**External:**
```
Legal team assesses breach notification requirements
  ↓
GDPR: 72 hours to notify supervisory authority
State laws: Various timelines (e.g., California: "without unreasonable delay")
  ↓
Communications team drafts customer notification
  ↓
Public disclosure (if required)
  ↓
Ongoing customer support (dedicated hotline, FAQ)
```

**Blameless Post-Mortems:**

Focus on systems and processes, not individuals.

**Template:**
```markdown
# Post-Mortem: SQL Injection Incident (2025-11-20)

## Summary
SQL injection vulnerability in search feature allowed unauthorized data access.

## Timeline (all times UTC)
- 14:32: Attacker begins probing search endpoint
- 14:45: First successful SQL injection (UNION query)
- 14:50: Attacker dumps user table (10,000 records)
- 15:10: SIEM alert on anomalous database queries
- 15:15: SOC analyst investigates, confirms SQL injection
- 15:20: Incident declared (P1), affected system isolated
- 15:45: Vulnerability identified and patched
- 16:00: Patch deployed to production
- 16:30: Verification scans confirm remediation

## Impact
- 10,000 user records accessed (usernames, email addresses, hashed passwords)
- No financial data or plaintext passwords compromised
- System offline for 30 minutes during patching

## Root Cause
- String concatenation used instead of parameterized queries
- Code review missed vulnerability
- SAST tool not configured to scan this codebase

## What Went Well
- SIEM detected anomaly within 20 minutes
- Incident response playbook followed
- Patched within 1 hour of detection
- No data exfiltration detected (attacker only read, didn't download)

## What Went Wrong
- Vulnerability existed for 6 months (introduced in v3.2.0)
- SAST not run on this repository
- Code review checklist didn't include SQL injection check

## Action Items
| Item | Owner | Due Date | Status |
|------|-------|----------|--------|
| Enable SAST for all repositories | DevOps | 2025-11-27 | In Progress |
| Update code review checklist | Security | 2025-11-22 | Done |
| Security training for developers | HR | 2025-12-15 | Planned |
| Implement WAF rules for SQLi | Security | 2025-11-21 | Done |
| Notify affected users | Legal | 2025-11-21 | Done |

## Lessons Learned
- Defense in depth: WAF would have blocked attack even if code had vulnerability
- Automated testing: SAST would have caught this before production
- Code review not sufficient alone

## Follow-Up
- Post-mortem review meeting: 2025-11-22 @ 10:00 AM
- Action items tracked in Jira (SECURITY-1234)
- Next post-mortem review: 2025-12-20
```

**Tools:**

| Category | Open Source | Commercial |
|----------|-------------|------------|
| SIEM | ELK Stack, Graylog, Wazuh | Splunk, Datadog, Sumo Logic |
| SOAR | TheHive, Shuffle | Palo Alto Cortex XSOAR, Splunk Phantom |
| EDR | Wazuh, OSQuery | CrowdStrike, SentinelOne, Carbon Black |
| NDR | Zeek, Suricata | Darktrace, Vectra, ExtraHop |
| Deception | - | Attivo, TrapX, Illusive |
| Threat Intel | MISP, OpenCTI | Recorded Future, ThreatConnect |
| Forensics | Autopsy, Volatility | EnCase, FTK, X-Ways |

---

## Trade-offs & Resolution Patterns

Real-world security requires balancing competing priorities. Common conflicts and their resolutions:

### Security vs. Usability

**Conflict**: MFA friction vs. account security

**Traditional Approach**: Require MFA on every login
- **Pro**: Maximum security
- **Con**: User frustration, support costs, workarounds

**Resolution**: Risk-based authentication
```python
def should_require_mfa(user, context):
    risk_score = 0

    # Known device?
    if context.device_id not in user.trusted_devices:
        risk_score += 3

    # Unusual location?
    if context.geo_location != user.usual_location:
        risk_score += 2

    # Unusual time?
    if context.hour < 6 or context.hour > 22:
        risk_score += 1

    # Sensitive operation?
    if context.action in ['wire_transfer', 'change_password']:
        risk_score += 5

    # Require MFA if risk score > threshold
    return risk_score >= 5
```

**Result**: MFA when risky, seamless when safe.

---

### Fail Secure vs. Availability

**Conflict**: Deny access on error vs. service uptime

**Example**: Authorization service down
- **Fail secure**: Deny all requests → service unavailable
- **Fail open**: Allow all requests → security bypassed

**Resolution**: Graceful degradation with cached permissions
```python
class AuthorizationService:
    def check_permission(self, user_id, resource, action):
        try:
            # Primary: Check against live permission database
            return self.db.has_permission(user_id, resource, action)
        except DatabaseError:
            # Fallback: Check local cache (max 5 minutes old)
            cached = self.cache.get(f"{user_id}:{resource}:{action}")
            if cached and (time.time() - cached.timestamp) < 300:
                log.warning("Using cached permissions (DB unavailable)")
                return cached.allowed
            else:
                # No cache or stale → fail secure
                log.error("Authorization DB down, no valid cache")
                alert_ops("Authorization system failure")
                return False  # Deny
```

**Trade-off**: Limited risk window (5 minutes cached permissions) vs. complete outage.

---

### Audit Everything vs. Privacy (GDPR)

**Conflict**: Logging PII vs. Right to Erasure

**Anti-Pattern**: Log everything including PII
```python
# BAD: Logs contain email addresses
log.info(f"User {user.email} accessed document {doc_id}")
```

**Resolution**: Pseudonymization with separate key vault
```python
# GOOD: Logs use pseudonymous ID
user_pseudo_id = hmac_sha256(user.email, secret_salt)
log.info(f"User {user_pseudo_id} accessed document {doc_id}")

# Separate table maps pseudo_id → email (encrypted)
# Right to Erasure: Delete mapping, logs remain but unlinkable
```

**Alternative**: Log retention policies
```
Event Type              Contains PII?   Retention
-------------------------------------------------------
Authentication          Email           90 days
Authorization           User ID (pseudo) 1 year
Data access             User ID (pseudo) 7 years (compliance)
Configuration changes   No PII          Indefinite
```

---

### Zero Trust vs. Developer Productivity

**Conflict**: Network microsegmentation vs. local development

**Problem**: Strict firewall rules prevent developers from testing locally
- **Option A**: Relax rules for dev environment → security gap
- **Option B**: Strict rules everywhere → developers can't work

**Resolution**: Separate development and production security postures
```yaml
# Development environment (relaxed)
---
firewall_rules:
  - allow: all traffic within VPC
  - deny: inbound from internet (except VPN)
monitoring: basic logging
mfa: optional

# Staging environment (transitional)
---
firewall_rules:
  - allow: whitelist of necessary service communication
  - deny: default deny
monitoring: full logging, anomaly detection
mfa: required

# Production environment (strict Zero Trust)
---
firewall_rules:
  - allow: explicit service-to-service (mTLS only)
  - deny: everything else
monitoring: full SIEM integration, threat detection
mfa: required with hardware tokens
microsegmentation: enabled
```

**Tooling**: Service mesh in prod, permissive for local dev
```bash
# Local development: Docker Compose (no mTLS)
docker-compose up

# Production: Istio service mesh (mTLS enforced)
kubectl apply -f istio-config.yaml
```

---

### Cost vs. Security (Encryption Overhead)

**Conflict**: Encrypt all data at rest vs. database performance

**Measurement**:
```
Encryption overhead:
  - AES-256-GCM (application-layer): 10-15% CPU
  - Transparent Database Encryption (TDE): 3-5% performance impact
  - Column-level encryption: 20-30% for encrypted columns
```

**Resolution**: Tiered encryption based on data classification
```sql
-- High-value data (credit cards, SSN): Application-layer encryption
CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    user_id INT,
    encrypted_card_data BYTEA,  -- AES-256-GCM encrypted in app
    encrypted_cvv BYTEA
);

-- Medium-value data (emails, names): Column-level encryption
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    email_encrypted VARCHAR(512)  -- Database-level encryption
);

-- Low-value data (public info): TDE only (full disk encryption)
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),  -- Not individually encrypted
    description TEXT
);
```

**Cost-Benefit**:
- Critical data: Accept performance hit for security
- Non-critical data: TDE sufficient (compliance requirement)

---

### Least Privilege vs. Operational Efficiency

**Conflict**: Fine-grained permissions vs. time to provision access

**Anti-Pattern**: Single "admin" role
```sql
-- BAD: Everyone is admin
GRANT ALL PRIVILEGES ON DATABASE prod TO app_user;
```

**Resolution**: Role-Based Access Control (RBAC) with preset roles
```sql
-- GOOD: Tiered roles
CREATE ROLE readonly_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_user;

CREATE ROLE app_user;
GRANT SELECT, INSERT, UPDATE ON orders, customers TO app_user;
GRANT SELECT ON products TO app_user;
-- NO DELETE, NO DROP

CREATE ROLE admin_user;
GRANT ALL PRIVILEGES ON DATABASE prod TO admin_user;

-- Users assigned to roles
GRANT readonly_user TO analyst@example.com;
GRANT app_user TO application_service_account;
```

**Tooling**: Infrastructure as Code for access management
```hcl
# Terraform: Provision IAM roles
resource "aws_iam_role" "developer" {
  name = "developer"

  assume_role_policy = jsonencode({
    Statement = [{
      Effect = "Allow"
      Action = "sts:AssumeRole"
      Principal = { AWS = var.developer_user_arns }
    }]
  })

  # Attach managed policy
  managed_policy_arns = [
    "arn:aws:iam::aws:policy/ReadOnlyAccess"
  ]
}
```

**Result**: Provisioning access takes minutes (via IaC), not days (via manual tickets).

---

## Anti-Patterns

Common security failures with real-world consequences:

### ❌ Security Theater

**Anti-Pattern**: Superficial controls without real risk reduction.

**Examples**:
- Password complexity rules (P@ssw0rd123!) that don't prevent breaches
- Annual security training (click-through, no retention)
- Firewall with allow-all rules
- "Security by checkbox" (compliance without actual security)

**Consequence**: False sense of security, resources wasted.

**Solution**:
- Focus on effective controls (MFA, password managers, breach detection)
- Measure security outcomes (MTTD, MTTR, incidents prevented)
- Continuous security training (phishing simulations, hands-on exercises)

---

### ❌ Checkbox Compliance

**Anti-Pattern**: Meeting letter of regulation, not spirit.

**Example**: PCI-DSS requirement for "strong cryptography"
- **Checkbox compliance**: Use any encryption (even weak DES)
- **Real security**: AES-256-GCM, TLS 1.3, no deprecated algorithms

**Consequence**: Pass audit, still vulnerable.

**Solution**:
- Understand why regulations exist
- Exceed minimum requirements where feasible
- Continuous security improvement, not one-time audit prep

---

### ❌ Perimeter-Only Security ("Hard Shell, Soft Center")

**Anti-Pattern**: Strong firewall, weak internal security.

**Example**:
```
Internet → Firewall (strong) → Internal network (no segmentation)
```

**Problem**: Once attacker breaches perimeter, lateral movement trivial.

**Consequence**: Single compromised laptop → entire network compromised.

**Solution**: Zero Trust, microsegmentation, assume breach.

---

### ❌ Security by Obscurity

**Anti-Pattern**: Relying on secrecy instead of cryptography.

**Examples**:
- Non-standard port numbers as security measure (port 2222 instead of 22)
- Custom encryption algorithms
- Hidden directories (`/admin-secret-panel-xyz`)

**Consequence**: Attackers find secrets via port scans, directory brute-forcing.

**Solution**:
- Use proven cryptographic algorithms
- Security through strong authentication, not secrecy

**Kerckhoffs's Principle**: System should be secure even if attacker knows how it works (except keys).

---

### ❌ Root Cause Whack-a-Mole

**Anti-Pattern**: Patching symptoms, not systemic issues.

**Example**:
```
Incident 1: SQL injection in /search endpoint → patch that endpoint
Incident 2: SQL injection in /admin endpoint → patch that endpoint
Incident 3: SQL injection in /api endpoint → patch that endpoint
```

**Problem**: Never fixed root cause (string concatenation instead of parameterized queries).

**Solution**: Systematic remediation
```python
# Fix systemically: Use ORM everywhere, ban raw SQL
# Code review checklist: No string concatenation for SQL
# SAST: Enforce parameterized queries
# Training: Educate developers on SQL injection
```

---

### ❌ Secret Sprawl

**Anti-Pattern**: Credentials in config files, environment variables, code.

**Examples**:
```python
# ❌ In code
API_KEY = "sk_live_abc123..."

# ❌ In version control
# .env file committed
DATABASE_PASSWORD=super_secret_123

# ❌ In container images
COPY secrets.json /app/

# ❌ In CI/CD logs
echo "Deploying with password: $DB_PASSWORD"
```

**Consequence**: Secrets leaked via GitHub, Docker Hub, CI logs.

**Solution**:
- Centralized secret management (Vault, AWS Secrets Manager)
- Pre-commit hooks (detect-secrets, TruffleHog)
- Never log secrets

---

### ❌ Alert Fatigue

**Anti-Pattern**: Too many false positives, real threats ignored.

**Example**:
```
SOC analyst receives 10,000 alerts/day
  → 99% false positives
  → Analyst ignores most alerts
  → Real breach goes unnoticed
```

**Consequence**: Signal-to-noise ratio too low, breaches missed.

**Solution**:
- Tune detection rules (reduce false positives)
- Prioritize alerts by severity and business impact
- Automate low-severity alerts (auto-remediation)
- SOAR platform for alert enrichment and deduplication

---

### ❌ Stale Dependencies ("If It Ain't Broke, Don't Update")

**Anti-Pattern**: Never updating libraries to "avoid breaking things".

**Example**:
```json
{
  "dependencies": {
    "lodash": "4.17.4"  // Vulnerable version from 2017
  }
}
```

**Consequence**: Accumulate vulnerabilities (technical and security debt).

**Solution**:
- Automated dependency updates (Dependabot, Renovate)
- Comprehensive test suite (safe to update)
- Regular update cycles (monthly minimum)

---

### ❌ Admin Access for Everyone

**Anti-Pattern**: Granting admin privileges to avoid permission issues.

**Example**:
```sql
-- Everyone is admin
GRANT ALL PRIVILEGES ON DATABASE prod TO every_developer;
```

**Consequence**: Accidental deletion, insider threats, privilege escalation.

**Solution**:
- Least privilege by default
- Just-in-time (JIT) access for elevated permissions
- Audit all admin actions

---

### ❌ No Incident Response Plan

**Anti-Pattern**: "We'll figure it out when it happens."

**Consequence**:
- Panic during actual incident
- Slow response (no playbooks)
- Poor communication (no escalation paths)
- Evidence destruction (no forensic readiness)

**Solution**:
- Document incident response plan
- Test with tabletop exercises (quarterly)
- Train IR team
- Pre-configure tools (SIEM, SOAR, forensics)

---

(Continuing in next message with Tool Ecosystem Map, Implementation Checklists, and remaining sections...)

## Tool Ecosystem Map

Mapping principles to implementing technologies:

| Principle | Open Source | Commercial | Notes |
|-----------|-------------|------------|-------|
| **I. Defense in Depth** | Nginx, ModSecurity, Fail2ban, Suricata | Cloudflare, Akamai, F5, Palo Alto | WAF, DDoS protection, IDS/IPS |
| **II. Least Privilege** | OpenLDAP, Keycloak, FreeIPA | Okta, Auth0, Azure AD | IAM, RBAC, attribute-based access |
| **III. Fail Secure** | - | - | Design pattern, not tool |
| **IV. Complete Mediation** | - | - | Architectural principle |
| **V. Economy of Mechanism** | - | - | Design philosophy |
| **VI. Secure by Default** | - | - | Configuration management |
| **VII. Zero Trust** | Pomerium, oauth2-proxy, Istio | Okta, Zscaler, Palo Alto Prisma | Identity-aware proxy, service mesh |
| **VIII. Cryptographic Agility** | OpenSSL, Libsodium, Bouncy Castle | AWS KMS, Azure Key Vault, Google Cloud KMS | Key management, crypto libraries |
| **IX. SDL** | SonarQube, OWASP ZAP, Semgrep, Trivy | Snyk, Veracode, Checkmarx, Fortify | SAST, DAST, SCA, IaC scanning |
| **X. Audit Everything** | ELK Stack, Graylog, Loki, Fluentd | Splunk, Datadog, Sumo Logic, Dynatrace | SIEM, log aggregation |
| **XI. Separation of Duties** | Git (branch protection), Jenkins (approval stages) | GitHub Enterprise, GitLab Ultimate | Workflow enforcement |
| **XII. Input Validation** | OWASP ESAPI, DOMPurify, validator.js | Imperva WAF, Signal Sciences, AWS WAF | Validation libraries, WAF |
| **XIII. Secrets Management** | HashiCorp Vault, SOPS, sealed-secrets | AWS Secrets Manager, Azure Key Vault, 1Password | Secret stores, encryption |
| **XIV. Vulnerability Mgmt** | Trivy, Grype, OWASP Dependency-Check | Snyk, Aqua Security, Rapid7, Tenable | Dependency scanning, vuln management |
| **XV. Immutable Infrastructure** | Docker, Packer, Terraform, ArgoCD | AWS AMIs, Azure VM Images, Google Compute | Container orchestration, IaC, GitOps |
| **XVI. Threat Modeling** | OWASP Threat Dragon, draw.io | Microsoft Threat Modeling Tool, IriusRisk | Threat modeling frameworks |
| **XVII. Supply Chain** | Syft (SBOM), Cosign (signing), in-toto | JFrog Xray, Sonatype Nexus, GitHub Advanced Security | SBOM generation, signing, provenance |
| **XVIII. Monitoring & IR** | TheHive, Wazuh, OSQuery, Velociraptor | Splunk, CrowdStrike, SentinelOne, Palo Alto Cortex | SIEM, SOAR, EDR, forensics |

### Category-Based Tool Map

**Identity & Access Management (IAM):**
- **Open Source**: Keycloak, Gluu, FreeIPA, Apache Syncope
- **Commercial**: Okta, Auth0, Ping Identity, ForgeRock, Azure AD, Google Workspace

**Security Testing:**
- **SAST**: SonarQube, Semgrep, Brakeman, Bandit | CodeQL (GitHub), Checkmarx, Veracode, Fortify
- **DAST**: OWASP ZAP, Nikto, w3af | Burp Suite Professional, Acunetix, Netsparker
- **SCA**: OWASP Dependency-Check, Trivy, Grype, OSV-Scanner | Snyk, Black Duck, WhiteSource
- **IaC Scanning**: Checkov, tfsec, Terrascan, kube-bench | Bridgecrew, Prisma Cloud, Aqua Security
- **Container Scanning**: Trivy, Clair, Anchore | Snyk Container, Aqua, Sysdig Secure
- **Secrets Scanning**: TruffleHog, GitLeaks, detect-secrets | GitGuardian, SpectralOps

**Web Application Firewall (WAF):**
- **Open Source**: ModSecurity, Naxsi, Shadow Daemon
- **Commercial**: Cloudflare WAF, AWS WAF, Azure WAF, Imperva, F5 Advanced WAF

**SIEM & Logging:**
- **Open Source**: ELK Stack (Elasticsearch, Logstash, Kibana), Graylog, Wazuh, OpenSearch
- **Commercial**: Splunk, Datadog, Sumo Logic, LogRhythm, QRadar, ArcSight

**SOAR (Security Orchestration):**
- **Open Source**: TheHive, Shuffle, StackStorm
- **Commercial**: Palo Alto Cortex XSOAR, Splunk Phantom, IBM Resilient, Swimlane

**Endpoint Detection & Response (EDR):**
- **Open Source**: Wazuh, OSQuery, Velociraptor
- **Commercial**: CrowdStrike Falcon, SentinelOne, Carbon Black, Microsoft Defender

**Network Detection & Response (NDR):**
- **Open Source**: Zeek, Suricata, Snort
- **Commercial**: Darktrace, Vectra, ExtraHop, Corelight

**Cloud Security Posture Management (CSPM):**
- **Open Source**: Prowler, CloudSploit, ScoutSuite
- **Commercial**: Wiz, Orca Security, Prisma Cloud, Lacework

**Secrets Management:**
- **Open Source**: HashiCorp Vault, SOPS, Sealed Secrets, Infisical
- **Commercial**: AWS Secrets Manager, Azure Key Vault, Google Secret Manager, 1Password, CyberArk

**Container & Kubernetes Security:**
- **Open Source**: Falco, Kubescape, kube-bench, kube-hunter, OPA/Gatekeeper
- **Commercial**: Aqua Security, Sysdig Secure, StackRox (Red Hat), Prisma Cloud

**Threat Intelligence:**
- **Open Source**: MISP, OpenCTI, TheHive
- **Commercial**: Recorded Future, ThreatConnect, Anomali, ThreatQuotient

**Vulnerability Management:**
- **Open Source**: OpenVAS, Nessus (free tier)
- **Commercial**: Tenable, Rapid7 InsightVM, Qualys, Nexpose

**Deception Technology:**
- **Commercial**: Attivo, TrapX, Illusive Networks, Cymmetria

**Forensics & Incident Response:**
- **Open Source**: Autopsy, Volatility, SIFT Workstation, GRR Rapid Response
- **Commercial**: EnCase, FTK, X-Ways, Cellebrite

**API Security:**
- **Open Source**: OWASP API Security Top 10, Swagger/OpenAPI validation
- **Commercial**: Salt Security, Traceable AI, Noname Security, 42Crunch

**Data Loss Prevention (DLP):**
- **Open Source**: OpenDLP, MyDLP
- **Commercial**: Symantec DLP, Digital Guardian, Forcepoint DLP, Microsoft Purview

---

## Implementation Checklists

Minimum viable implementation for each principle:

### I. Defense in Depth
- [ ] Deploy WAF (ModSecurity, AWS WAF, Cloudflare)
- [ ] Configure network segmentation (VPC, subnets, security groups)
- [ ] Enable TLS everywhere (HTTPS, enforce HTTP → HTTPS redirect)
- [ ] Implement input validation at application layer
- [ ] Deploy intrusion detection system (IDS/IPS)
- [ ] Enable encryption at rest (database, file storage)
- [ ] Configure firewall rules (default deny)
- [ ] Deploy rate limiting (API gateway, application layer)

### II. Least Privilege
- [ ] Audit all user/service account permissions
- [ ] Remove unnecessary admin accounts
- [ ] Implement RBAC (role-based access control)
- [ ] Configure service accounts with minimal permissions
- [ ] Enable time-bounded credentials (STS, temporary tokens)
- [ ] Implement JIT (just-in-time) access for privileged operations
- [ ] Regular access reviews (quarterly minimum)
- [ ] Remove default/unused accounts

### III. Fail Secure
- [ ] Test failure modes (disconnect database, kill auth service)
- [ ] Verify system denies access on error (not allows)
- [ ] Implement circuit breakers for dependencies
- [ ] Configure graceful degradation with security maintained
- [ ] Audit exception handling (no fail-open paths)
- [ ] Alert on service failures (monitoring)

### IV. Complete Mediation
- [ ] Remove permission caching (or limit TTL to < 5 minutes)
- [ ] Validate authorization on every sensitive operation
- [ ] Implement token revocation checking (logout, password change)
- [ ] Test: Revoke permissions, verify immediate effect
- [ ] Audit authorization checks in code (code review checklist)

### V. Economy of Mechanism
- [ ] Use standard crypto libraries (no custom implementations)
- [ ] Simplify authentication flows
- [ ] Reduce lines of security-critical code
- [ ] Minimize trusted computing base (TCB)
- [ ] Replace complex security logic with proven patterns

### VI. Secure by Default
- [ ] Disable HTTP (HTTPS only)
- [ ] Enforce authentication (no anonymous access by default)
- [ ] Enable security headers (CSP, HSTS, X-Frame-Options)
- [ ] Disable debug mode in production
- [ ] Remove default credentials
- [ ] Enable encryption at rest by default
- [ ] Configure restrictive CORS (not `*`)
- [ ] Disable unnecessary services/ports

### VII. Zero Trust
- [ ] Implement MFA for all users (no exceptions)
- [ ] Deploy identity-aware proxy (Pomerium, Google IAP)
- [ ] Enable mTLS for service-to-service communication
- [ ] Implement network microsegmentation (Kubernetes Network Policies)
- [ ] Deploy device posture checking
- [ ] Remove VPN (replace with Zero Trust Network Access)
- [ ] Continuous verification for sensitive operations

### VIII. Cryptographic Agility
- [ ] Abstract cryptographic operations (algorithm ID in encrypted data)
- [ ] Version all encrypted data (metadata: `{version, algorithm, ciphertext}`)
- [ ] Document algorithm migration process
- [ ] Test algorithm rotation (dev environment)
- [ ] Prepare for quantum-resistant algorithms (roadmap)
- [ ] Configure TLS cipher suites (prefer server-side ordering)

### IX. Secure Development Lifecycle
- [ ] Conduct threat modeling for new features
- [ ] Add security requirements to project documentation
- [ ] Implement security code review checklist
- [ ] Deploy SAST in CI/CD (SonarQube, Semgrep)
- [ ] Deploy DAST (OWASP ZAP, scheduled scans)
- [ ] Enable dependency scanning (Dependabot, Snyk)
- [ ] Implement pre-commit hooks (secrets scanning)
- [ ] Require security sign-off for production deploys
- [ ] Conduct penetration testing (annually or per major release)

### X. Audit Everything
- [ ] Implement structured logging (JSON format)
- [ ] Log authentication events (success and failure)
- [ ] Log authorization decisions (especially denials)
- [ ] Log data access to sensitive resources
- [ ] Log configuration changes
- [ ] Deploy centralized logging (SIEM: ELK, Splunk)
- [ ] Configure log retention policies (per compliance requirements)
- [ ] Implement tamper-evident logging (integrity protection)
- [ ] Alert on security events (failed logins, permission denials)

### XI. Separation of Duties
- [ ] Enable branch protection (require 2 approvals for main branch)
- [ ] Implement code review process (author ≠ approver)
- [ ] Separate deployment approvals from code authorship
- [ ] Implement maker-checker for financial transactions
- [ ] Use M-of-N secret sharing for master keys (3 of 5)
- [ ] Audit admin actions (require approval for sensitive operations)

### XII. Input Validation & Output Encoding
- [ ] Implement input validation schemas (OpenAPI, Pydantic)
- [ ] Validate all user input at API boundary
- [ ] Use parameterized queries (no string concatenation for SQL)
- [ ] Implement output encoding (HTML escape, URL encode)
- [ ] Deploy Content Security Policy (CSP headers)
- [ ] Configure CORS (whitelist specific origins)
- [ ] Implement file upload validation (magic bytes, size limits)
- [ ] Deploy WAF with injection attack rules

### XIII. Secure Secrets Management
- [ ] Remove hardcoded secrets from code
- [ ] Deploy secret management solution (Vault, AWS Secrets Manager)
- [ ] Implement secret rotation (90-day maximum for high-value)
- [ ] Use temporary credentials where possible (IAM roles, STS)
- [ ] Enable pre-commit hooks for secret detection
- [ ] Scan Git history for leaked secrets
- [ ] Audit secret access (who accessed what, when)
- [ ] Implement break-glass procedures for emergency access

### XIV. Vulnerability Management
- [ ] Deploy dependency scanning (daily)
- [ ] Deploy container image scanning (on build)
- [ ] Deploy infrastructure scanning (weekly)
- [ ] Define remediation SLAs (Critical: 24h, High: 7d, Medium: 30d)
- [ ] Implement automated dependency updates (Dependabot)
- [ ] Deploy compensating controls for unpatchable vulnerabilities
- [ ] Establish vulnerability disclosure program (bug bounty)
- [ ] Track MTTR (Mean Time To Remediate)

### XV. Immutable Infrastructure
- [ ] Implement infrastructure as code (Terraform, CloudFormation)
- [ ] Build immutable container images (Docker, Packer)
- [ ] Deploy via GitOps (ArgoCD, FluxCD)
- [ ] Disable SSH access to production (or break-glass only)
- [ ] Implement configuration drift detection
- [ ] Sign container images (Cosign, Notary)
- [ ] Verify image provenance (SLSA)
- [ ] Replace compromised instances (don't repair)

### XVI. Threat Modeling
- [ ] Create data flow diagrams (DFDs) for critical systems
- [ ] Conduct STRIDE analysis for each component
- [ ] Document trust boundaries
- [ ] Identify and prioritize threats
- [ ] Define mitigations for high-priority threats
- [ ] Test mitigations (security test cases)
- [ ] Review threat model annually
- [ ] Update threat model with architecture changes

### XVII. Supply Chain Security
- [ ] Generate SBOM for all deployments (Syft, CycloneDX)
- [ ] Pin dependency versions (lock files)
- [ ] Verify package signatures (npm audit signatures)
- [ ] Deploy private package registry (Verdaccio, Artifactory)
- [ ] Prevent dependency confusion (namespace scoping)
- [ ] Scan dependencies continuously (Snyk, Dependabot)
- [ ] Vet new dependencies (checklist)
- [ ] Sign build artifacts (Cosign, GPG)
- [ ] Implement SLSA provenance (level 3+ for critical systems)

### XVIII. Security Monitoring & Incident Response
- [ ] Deploy SIEM (ELK, Splunk, Datadog)
- [ ] Configure detection rules (signature-based, anomaly detection)
- [ ] Integrate threat intelligence feeds
- [ ] Document incident response plan
- [ ] Define severity classification (P0-P3)
- [ ] Create incident response playbooks (ransomware, phishing, data breach)
- [ ] Establish communication plan (internal and external)
- [ ] Conduct tabletop exercises (quarterly)
- [ ] Measure MTTD and MTTR
- [ ] Implement SOAR for automation (optional)

---

## Security Maturity Model

Assess current state and set improvement goals:

### Level 0 - Ad Hoc
**Characteristics:**
- No security team or designated security personnel
- Reactive security (respond to incidents only)
- Credentials in code, no secrets management
- No security testing
- Manual, inconsistent patching
- No incident response plan
- Compliance-driven (minimum effort)

**Action**: Establish security fundamentals
- Hire security champion or contractor
- Implement basic IAM and MFA
- Deploy secrets management
- Enable basic logging

---

### Level 1 - Basic Controls
**Characteristics:**
- Part-time security champion or small team
- Firewall, antivirus, basic logging
- Passwords + optional MFA (executives only)
- Manual security testing before major releases
- Incident response via email thread (ad-hoc)
- Quarterly vulnerability scans
- Basic compliance (annual audits)

**Action**: Formalize security processes
- Implement SAST/DAST in CI/CD
- Enforce MFA for all users
- Document incident response procedures
- Establish regular patching cadence

---

### Level 2 - Repeatable Processes
**Characteristics:**
- Dedicated security team (2-5 people) or outsourced SOC
- SAST/DAST in CI/CD pipelines
- Centralized secrets management (Vault, cloud KMS)
- Defined incident response playbooks (tested)
- Regular patching cadence (monthly)
- Security training for developers (annual)
- Dependency scanning automated

**Action**: Measure and improve
- Define security KPIs (MTTD, MTTR, vuln count)
- Implement threat modeling for new features
- Deploy SIEM with correlation rules
- Conduct quarterly tabletop exercises

---

### Level 3 - Defined & Measured
**Characteristics:**
- Security team integrated into SDLC
- Security metrics tracked and reported to leadership
  - MTTD, MTTR, vulnerability SLA compliance
  - Patch coverage, MFA adoption, incident count
- Threat modeling required for new features
- Zero Trust architecture partially implemented
- SIEM with automated alerting and correlation
- Tabletop exercises quarterly
- Security champions embedded in product teams
- Annual penetration testing

**Action**: Automate and optimize
- Deploy SOAR for automated incident response
- Implement policy-as-code (OPA, Sentinel)
- Continuous compliance monitoring
- Red team/purple team exercises

---

### Level 4 - Managed & Automated
**Characteristics:**
- Security fully integrated into DevOps (DevSecOps)
- Automated security testing gates (block on critical findings)
- Policy-as-code enforced (OPA/Gatekeeper, Sentinel)
- Continuous compliance monitoring (automated evidence collection)
- SOAR platform for automated response
- Red team/purple team exercises (bi-annually)
- Proactive threat hunting (dedicated team)
- Security chaos engineering (simulate attacks)
- Bug bounty program (active participation)

**Action**: Industry leadership
- Publish security research and advisories
- Contribute to open source security tools
- Speak at security conferences
- Achieve advanced certifications (FedRAMP, ISO 27001)

---

### Level 5 - Optimizing (Industry-Leading)
**Characteristics:**
- Security as competitive advantage (marketing point)
- AI/ML-driven anomaly detection and automated response
- Predictive vulnerability management (EPSS-based prioritization)
- Security chaos engineering (regular "failure Fridays")
- Industry-leading bug bounty program (top payouts)
- Published security research/advisories (CVEs, whitepapers)
- Open source security tool contributions
- Zero trust fully implemented (microsegmentation, mTLS)
- Formal verification for critical components
- Real-time threat intelligence integration
- Sub-hour MTTR for critical incidents

**Characteristics**: Continuous innovation, security thought leadership

---

## Organizational Enablement

Security excellence requires cultural transformation, not just technology:

### Executive Sponsorship

**Top-Down Mandate:**
- CEO/CTO communication: "Security is a strategic priority"
- Board-level security reporting (quarterly minimum)
- CISO reports to CEO (not CTO/CIO) to avoid conflicts of interest
- Security included in company-wide OKRs

**Budget Allocation:**
- Dedicate 10-15% of engineering budget to security platform
- Industry benchmarks: 5-10% of IT budget for security tools
- Budget for training, certifications, conferences

**Success Metrics:**
- Security KPIs in executive dashboard
  - Mean Time To Detect (MTTD): < 1 hour
  - Mean Time To Respond (MTTR): < 4 hours
  - Vulnerability SLA compliance: > 95%
  - Phishing simulation click rate: < 5%
  - MFA adoption: 100%
- Incidents reviewed in leadership meetings
- Customer trust metrics (NPS impact of security)

**Accountability:**
- Security incidents = CEO-level escalation
- Security metrics in manager performance reviews
- Public commitments (security transparency report)

---

### Incentive Alignment

**Reward Data Quality:**
- Engineer bonuses tied to security metrics (vulnerabilities fixed, incidents prevented)
- Bug bounty rewards (internal program)
- Security MVP awards (quarterly)
- Fast-track promotions for security contributions

**Penalize Silos:**
- Manager reviews include cross-team collaboration metrics
- Reward knowledge sharing (internal tech talks, documentation)

**Celebrate Success:**
- Spotlight teams improving security posture
- Public recognition for incident responders
- Share success stories company-wide

**Blameless Culture:**
- Blameless post-mortems (focus on systems, not individuals)
- Psychological safety to report security issues
- No punishment for honest mistakes (only negligence)

---

### Training Programs

**For Developers:**
- **Secure Coding Bootcamp** (2-3 days)
  - OWASP Top 10 deep dive
  - Secure coding patterns (input validation, authentication, cryptography)
  - Hands-on labs (exploit and fix vulnerabilities)
  - Language-specific training (Java, Python, JavaScript, Go)

- **Threat Modeling Workshop** (1 day)
  - STRIDE methodology
  - Data flow diagrams
  - Attack trees
  - Hands-on: Threat model new feature

- **Security Tools Training** (ongoing)
  - SAST/DAST tool usage
  - Secrets management (Vault)
  - Container security (Trivy, Falco)

**For Security Engineers:**
- **Advanced Penetration Testing** (5 days)
  - Web application pentesting
  - Network penetration testing
  - Cloud security assessment
  - Certification prep (OSCP, CEH)

- **Incident Response & Forensics** (3 days)
  - IR playbook development
  - Forensic analysis (disk, memory, network)
  - Malware analysis
  - Hands-on IR simulation

- **Cloud Security** (2 days)
  - AWS/Azure/GCP security services
  - IAM best practices
  - Container orchestration security (Kubernetes)

**For Leadership:**
- **Security Governance** (1 day)
  - Risk management frameworks (NIST CSF, ISO 27001)
  - Regulatory compliance (GDPR, PCI-DSS, HIPAA)
  - Incident escalation procedures
  - Board-level security reporting

**For Everyone:**
- **Security Awareness Training** (quarterly)
  - Phishing simulations (monthly)
  - Social engineering awareness
  - Physical security (badge tailgating)
  - Data classification and handling

**Certification Support:**
- Paid certifications: CISSP, OSCP, CCSP, GIAC
- Study time during work hours
- Bonuses for certifications earned

---

### Community of Practice

**Security Guild:**
- Monthly meetups (brown bags, lightning talks)
- Show-and-tell (recent vulnerabilities fixed, tools adopted)
- Knowledge sharing (Confluence wiki, internal blog)
- Book club (security books, papers)

**Office Hours:**
- Security team availability for consultation (Slack channel)
- Architecture review sessions (pre-design phase)
- Pair programming on security features

**Internal Blog:**
- Document lessons learned from incidents
- Security best practices (internal wiki)
- Tool guides (how to use SAST, secrets management)

**Mentorship:**
- Pair senior and junior security engineers
- Security champions mentor product engineers
- Rotation programs (developers join security team for 3 months)

---

### Conway's Law Considerations

**Domain-Aligned Teams:**
- Product teams own security for their domain (not centralized bottleneck)
- Security team provides tooling and consultation (not execution)
- Example: Payments team owns PCI-DSS compliance for payment systems

**Platform Team:**
- Builds self-serve security infrastructure (SIEM, secrets management, CI/CD security gates)
- Not execution bottleneck for application security

**Data Governance:**
- Enabling function, not control tower
- Set security policies, provide tooling
- Teams self-serve within guardrails

**Avoid:**
- Centralized security team as single point of failure for all security tasks
- Security review as final gate (integrate earlier)

---

### Change Management

**Pilot Program:**
- Start with one product team (most mature or most motivated)
- Prove value over 3 months (metrics: vulnerabilities fixed, incidents prevented)
- Expand to other teams based on success

**Quick Wins:**
- Fix most painful security issue in 2 weeks → build credibility
- Examples: Enable MFA (immediate impact), deploy WAF (block attacks), fix critical vulnerability

**Migration Path:**
- Parallel run old and new security processes
- Gradual cutover (not big-bang)
- Example: Run SAST alongside manual code review for 3 months before full automation

**Sunset Legacy:**
- Decommission old systems after 6-month overlap
- Document migration (runbooks)
- Celebrate retirement of insecure systems

---

### Communication Strategy

**Transparency:**
- Publish security transparency report (annually)
  - Incidents disclosed (aggregate statistics)
  - Bug bounty stats
  - Compliance certifications
- Security roadmap visible to entire company

**Regular Updates:**
- Monthly security newsletter (vulnerabilities patched, new tools)
- Quarterly all-hands presentation (CISO)
- Real-time incident updates (status page)

**Customer Communication:**
- Security landing page (security.example.com)
  - Encryption standards
  - Compliance certifications
  - Vulnerability disclosure policy
  - Security contact
- Customer security questionnaire (self-serve)
- SOC 2 Type II report available (NDA)

---

## Learning Paths

### 30-Day Security Quickstart (For Developers)

**Goal**: Understand common vulnerabilities and how to prevent them.

**Week 1: OWASP Top 10** (10 hours)
- Read: OWASP Top 10 2021 (https://owasp.org/Top10/)
- Practice: Hack vulnerable apps
  - OWASP WebGoat (hands-on labs)
  - DVWA (Damn Vulnerable Web Application)
  - HackTheBox (beginner boxes)
- Outcome: Understand injection, broken auth, XSS, CSRF

**Week 2: Secure Coding** (10 hours)
- Read: OWASP Secure Coding Practices
- Practice:
  - Fix vulnerabilities in sample code (GitHub Security Lab)
  - Run SAST tool on own project (SonarQube, Semgrep)
- Outcome: Write secure code (input validation, output encoding, parameterized queries)

**Week 3: Threat Modeling** (8 hours)
- Read: Threat Modeling Manifesto (https://www.threatmodelingmanifesto.org/)
- Tool: Microsoft Threat Modeling Tool or OWASP Threat Dragon
- Practice: Threat model one feature in your application
- Outcome: Identify threats systematically (STRIDE)

**Week 4: Security Testing** (12 hours)
- Read: OWASP Testing Guide
- Tools:
  - OWASP ZAP (DAST)
  - npm audit, pip-audit (dependency scanning)
  - TruffleHog (secrets scanning)
- Practice: Scan your application, fix findings
- Outcome: Integrate security testing into CI/CD

**Final Project**: Secure a vulnerable app end-to-end
- Deploy WebGoat or DVWA
- Scan with ZAP
- Fix all vulnerabilities
- Document mitigations

---

### 3-Month Security Engineer Deep Dive

**Goal**: Become proficient in offensive and defensive security.

**Month 1: Web Application Security** (40 hours)
- **Week 1-2**: PortSwigger Web Security Academy
  - SQL injection, XSS, CSRF, authentication attacks
  - Complete all labs (apprentice and practitioner levels)
- **Week 3**: OWASP Top 10 deep dive
  - Read whitepapers for each vulnerability
  - Practice exploitation and mitigation
- **Week 4**: Burp Suite Professional training
  - Proxy, scanner, intruder, repeater
  - Extension development (Python)
- **Outcome**: Confidently assess web application security

**Month 2: Cloud Security** (40 hours)
- **Week 1**: AWS Security Fundamentals
  - IAM, security groups, VPCs, KMS
  - AWS Well-Architected Framework (security pillar)
- **Week 2**: Azure/GCP Security (choose based on environment)
  - Azure RBAC, Key Vault, Security Center
  - GCP IAM, Cloud Armor, Security Command Center
- **Week 3**: Container Security
  - Docker security best practices
  - Kubernetes security (RBAC, Network Policies, Pod Security)
  - Scanning (Trivy, Anchore)
- **Week 4**: Cloud Security Assessment
  - Scout Suite, Prowler, CloudSploit
  - Assess cloud environment, document findings
- **Outcome**: Secure cloud-native applications

**Month 3: Incident Response & Forensics** (40 hours)
- **Week 1**: Malware Analysis
  - Static analysis (strings, PE headers)
  - Dynamic analysis (sandbox, debugger)
  - Reverse engineering basics (Ghidra, IDA Free)
- **Week 2**: Network Forensics
  - Wireshark packet analysis
  - Zeek log analysis
  - Detect C2 traffic, data exfiltration
- **Week 3**: Disk & Memory Forensics
  - Autopsy (disk forensics)
  - Volatility (memory forensics)
  - Timeline reconstruction
- **Week 4**: Incident Response Simulation
  - Hands-on IR lab (CyberDefenders, BlueTeamLabs)
  - Respond to simulated breach
  - Write post-mortem report
- **Outcome**: Lead incident response investigations

**Capstone Project**: Red Team vs. Blue Team CTF
- Join HackTheBox or TryHackMe team
- Complete 10 machines (attack path: reconnaissance → exploitation → privilege escalation)
- Defend vulnerable infrastructure (blue team simulation)

---

### 1-Day Executive Security Overview

**Goal**: Decide whether to invest in security program expansion.

**Morning (4 hours): Understanding**
- **Read**:
  - "2024 Verizon Data Breach Investigations Report" (executive summary)
  - "Cost of a Data Breach Report" (IBM)
  - This manifesto's principles overview
  - "Why Amazon Chose TLA+" (formal methods in cloud)

- **Watch**:
  - "Security is a Product Feature" (tech talk, 30 min)
  - Ransomware attack simulation (YouTube, 15 min)

- **Outcome**: Understand modern threat landscape and financial impact

**Afternoon (4 hours): Decision Framework**
- **Assess**:
  - Which systems are critical? (revenue-generating, customer-facing, data stores)
  - What is cost of breach? (revenue loss + legal + reputation)
  - Current security posture? (use maturity model, self-assessment)

- **Calculate ROI**:
  - Cost of security investment (tools + headcount + training)
  - Expected risk reduction (% decrease in breach probability)
  - Formula: `ROI = (Breach Cost × Risk Reduction) / Security Investment`
  - Example: ($10M breach × 50% risk reduction) / $1M investment = 400% ROI

- **Decide**:
  - Start with Level 1-2 (basics: MFA, SAST, logging) or jump to Level 3 (Zero Trust, SIEM)?
  - Build internal team or outsource to MSSP?
  - Immediate actions (30-day plan)
  - Long-term roadmap (1-year plan)

- **Plan**:
  - Budget allocation (Year 1: $X, Year 2: $Y)
  - Hiring plan (CISO, security engineers, SOC analysts)
  - Tool procurement (SIEM, SAST, SOAR)
  - Training budget (certifications, bootcamps)

**Outcome**: Informed decision on security investment with board-ready business case

---

## Modern Architecture Considerations

### Cloud-Native Security

**Shared Responsibility Model:**
```
Cloud Provider Responsible For:
  - Physical security of data centers
  - Hypervisor security
  - Network infrastructure
  - Hardware (compute, storage, network)

Customer Responsible For:
  - IAM (users, roles, policies)
  - Data encryption (at rest, in transit)
  - Application security (code, dependencies)
  - OS patching (if IaaS)
  - Network configuration (security groups, VPCs)
  - Backup and disaster recovery
```

**Cloud-Specific Security Services:**

**AWS:**
- **IAM**: Identity and Access Management (roles, policies, MFA)
- **GuardDuty**: Threat detection (ML-based anomaly detection)
- **Security Hub**: Centralized security findings (aggregates from multiple services)
- **CloudTrail**: Audit logging (all API calls)
- **KMS**: Key management service (envelope encryption)
- **Secrets Manager**: Secrets rotation and retrieval
- **WAF**: Web Application Firewall
- **Shield**: DDoS protection
- **Macie**: Data classification and PII discovery

**Azure:**
- **Azure AD**: Identity (MFA, Conditional Access)
- **Security Center / Defender for Cloud**: CSPM + threat protection
- **Sentinel**: Cloud-native SIEM
- **Key Vault**: Secrets, keys, certificates
- **Application Gateway WAF**: Web application firewall
- **DDoS Protection**: Network-level protection
- **Purview**: Data governance and classification

**GCP:**
- **IAM**: Identity and access management
- **Security Command Center**: CSPM and threat detection
- **Cloud Armor**: DDoS and WAF
- **KMS**: Key management
- **Secret Manager**: Secrets storage
- **Chronicle**: SIEM (Google Cloud)
- **Binary Authorization**: Deploy-time policy enforcement

**Cloud Security Best Practices:**
```yaml
# Infrastructure as Code (Terraform)
# Enforce security baseline
resource "aws_s3_bucket" "data" {
  bucket = "my-secure-bucket"

  # Encryption at rest (required)
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  # Block public access (required)
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true

  # Versioning (backup protection)
  versioning {
    enabled = true
  }

  # Logging (audit trail)
  logging {
    target_bucket = aws_s3_bucket.logs.id
    target_prefix = "data-bucket-logs/"
  }
}
```

---

### Microservices Security

**Service-to-Service Authentication:**
- **mTLS (mutual TLS)**: Both client and server authenticate with certificates
- **Service Mesh**: Istio, Linkerd, Consul Connect (automatic mTLS)
- **JWT tokens**: Service identity tokens (short-lived)

**Example: Istio mTLS:**
```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: production
spec:
  mtls:
    mode: STRICT  # Require mTLS for all service communication
```

**API Gateway as Policy Enforcement Point:**
```
Client → API Gateway → [Microservices]

API Gateway responsibilities:
  - Authentication (verify JWT)
  - Authorization (RBAC/ABAC)
  - Rate limiting (per user, per IP)
  - Request validation (schema)
  - TLS termination
  - Logging and monitoring
```

**Strangler Fig Pattern (Legacy Migration):**
```
Phase 1: Legacy monolith handles all traffic
Phase 2: Route new features to microservices, legacy handles old features
Phase 3: Gradually migrate old features to microservices
Phase 4: Retire legacy monolith

Security consideration: Consistent auth across legacy and microservices
  → Use API gateway as single auth point
  → Shared JWT validation
```

---

### Serverless Security

**Function-Level IAM:**
```yaml
# AWS Lambda function with least privilege IAM role
LambdaExecutionRole:
  Type: AWS::IAM::Role
  Properties:
    AssumeRolePolicyDocument:
      Statement:
        - Effect: Allow
          Principal:
            Service: lambda.amazonaws.com
          Action: 'sts:AssumeRole'
    Policies:
      - PolicyName: LambdaPolicy
        PolicyDocument:
          Statement:
            - Effect: Allow
              Action:
                - 'dynamodb:GetItem'  # Only read from specific table
              Resource: 'arn:aws:dynamodb:us-east-1:123456789:table/Orders'
            - Effect: Allow
              Action:
                - 'logs:CreateLogGroup'  # Logging
                - 'logs:CreateLogStream'
                - 'logs:PutLogEvents'
              Resource: 'arn:aws:logs:*:*:*'
```

**Cold Start Security:**
- Secrets fetched on first invocation → cached for warm starts
- Risk: Secrets may not rotate if function stays warm
- Mitigation: Periodic secret refresh (every N invocations)

**Dependency Management:**
- Minimize dependencies (smaller attack surface, faster cold starts)
- Layer shared dependencies (security scanner only scans layers once)

**Input Validation:**
- Validate event payloads (API Gateway request validation)
- Never trust event source (even internal triggers)

---

### Container Security

**Image Security:**
```dockerfile
# Multi-stage build (minimal final image)
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Minimal runtime image (distroless)
FROM gcr.io/distroless/nodejs18-debian11
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules

# Non-root user (security)
USER nonroot

# Immutable filesystem
# (Read-only root filesystem enforced by Kubernetes Pod Security)

CMD ["dist/server.js"]
```

**Benefits**:
- Minimal attack surface (no shell, no package manager)
- Non-root user (privilege escalation harder)
- Smaller image (faster scans, less storage)

**Runtime Security (Falco):**
```yaml
# Falco rule: Detect unexpected file writes
- rule: Write below root
  desc: Detect writes below / (should be read-only)
  condition: >
    write and
    container and
    fd.directory = / and
    not fd.name in (/proc, /sys, /dev)
  output: "File write below root (user=%user.name command=%proc.cmdline file=%fd.name)"
  priority: WARNING
```

**Kubernetes Security:**

**Pod Security Standards:**
```yaml
# Enforce restricted Pod Security Standard
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: latest
```

**Network Policies:**
```yaml
# Default deny all traffic
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
---
# Allow specific service communication
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
spec:
  podSelector:
    matchLabels:
      app: backend
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
```

**RBAC:**
```yaml
# Service account with limited permissions
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-serviceaccount
  namespace: production
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: app-role
  namespace: production
rules:
  - apiGroups: [""]
    resources: ["configmaps", "secrets"]
    verbs: ["get", "list"]  # Read-only
  # No permissions to modify or delete
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-rolebinding
  namespace: production
subjects:
  - kind: ServiceAccount
    name: app-serviceaccount
roleRef:
  kind: Role
  name: app-role
  apiGroup: rbac.authorization.k8s.io
```

---

## Compliance Mapping

Map principles to compliance frameworks:

### OWASP Top 10 (2021)

| OWASP Category | Principles | Mitigations |
|----------------|------------|-------------|
| **A01 - Broken Access Control** | II (Least Privilege), IV (Complete Mediation) | RBAC, authorization checks, audit logs |
| **A02 - Cryptographic Failures** | VIII (Cryptographic Agility), XIII (Secrets) | TLS, encryption at rest, key management |
| **A03 - Injection** | XII (Input Validation) | Parameterized queries, input validation, output encoding |
| **A04 - Insecure Design** | XVI (Threat Modeling), IX (SDL) | Threat modeling, secure architecture review |
| **A05 - Security Misconfiguration** | VI (Secure by Default), XV (Immutable Infrastructure) | Security baselines, IaC, configuration management |
| **A06 - Vulnerable Components** | XIV (Vulnerability Management), XVII (Supply Chain) | Dependency scanning, SCA, patching |
| **A07 - Identification & Auth Failures** | II (Least Privilege), VII (Zero Trust) | MFA, password policies, session management |
| **A08 - Software & Data Integrity Failures** | XVII (Supply Chain), XV (Immutable Infrastructure) | Code signing, SBOM, provenance verification |
| **A09 - Logging & Monitoring Failures** | X (Audit Everything), XVIII (Monitoring) | Centralized logging, SIEM, alerting |
| **A10 - Server-Side Request Forgery** | XII (Input Validation), I (Defense in Depth) | URL validation, network segmentation, WAF |

### NIST Cybersecurity Framework

| NIST Function | Principles | Implementation |
|---------------|------------|----------------|
| **Identify** | XVI (Threat Modeling), XVII (Supply Chain) | Asset inventory, risk assessment, SBOM |
| **Protect** | I-XV (all core principles) | Access controls, encryption, secure SDLC |
| **Detect** | X (Audit), XIII (Monitoring) | SIEM, anomaly detection, intrusion detection |
| **Respond** | XVIII (Incident Response) | IR playbooks, SOAR, communication plan |
| **Recover** | XV (Immutable Infrastructure) | Backups, disaster recovery, business continuity |

### CIS Controls (v8)

| CIS Control | Principles | Tools |
|-------------|------------|-------|
| **1. Inventory of Assets** | XVII (Supply Chain) | Asset management, CMDB, SBOM |
| **2. Inventory of Software** | XIV (Vulnerability Management) | SCA, dependency scanning |
| **3. Data Protection** | VIII (Cryptographic Agility), XIII (Secrets) | Encryption, DLP, tokenization |
| **4. Secure Configuration** | VI (Secure by Default), XV (IaC) | CIS benchmarks, IaC, drift detection |
| **5. Account Management** | II (Least Privilege) | IAM, RBAC, access reviews |
| **6. Access Control Management** | IV (Complete Mediation), VII (Zero Trust) | MFA, PAM, JIT access |
| **7. Continuous Vulnerability Management** | XIV (Vulnerability Management) | Scanning, patching, CSPM |
| **8. Audit Log Management** | X (Audit Everything) | SIEM, log aggregation, retention |
| **9. Email & Web Browser Protections** | I (Defense in Depth) | Email filtering, browser isolation |
| **10. Malware Defenses** | I (Defense in Depth) | Antivirus, EDR, sandboxing |
| **11. Data Recovery** | XV (Immutable Infrastructure) | Backups, replication, DR testing |
| **12. Network Infrastructure Management** | VII (Zero Trust), I (Defense in Depth) | Segmentation, firewalls, microsegmentation |
| **13. Network Monitoring** | XVIII (Monitoring) | NDR, IDS/IPS, flow analysis |
| **14. Security Awareness** | IX (SDL) | Training, phishing simulations |
| **15. Service Provider Management** | XVII (Supply Chain) | Vendor assessments, SLAs |
| **16. Application Software Security** | IX (SDL), XII (Input Validation) | SAST, DAST, code review |
| **17. Incident Response Management** | XVIII (Incident Response) | IR plan, SOAR, tabletop exercises |
| **18. Penetration Testing** | IX (SDL) | Red team, bug bounty, pentest |

### ISO 27001:2022

| ISO 27001 Control | Principles | Implementation |
|-------------------|------------|----------------|
| **A.5 - Organizational Controls** | Organizational Enablement | Policies, training, roles |
| **A.6 - People Controls** | Organizational Enablement | Background checks, training, NDAs |
| **A.7 - Physical Controls** | I (Defense in Depth) | Access control, surveillance |
| **A.8 - Technological Controls** | I-XVIII (all principles) | Technical security controls |

**Specific mappings**:
- **A.8.1 - User endpoints**: Principle II (Least Privilege), EDR
- **A.8.2 - Privileged access rights**: Principle II, PAM, MFA
- **A.8.3 - Information access restriction**: Principle IV (Complete Mediation)
- **A.8.4 - Access to source code**: Principle XI (Separation of Duties), code review
- **A.8.5 - Secure authentication**: Principle VII (Zero Trust), MFA
- **A.8.6 - Capacity management**: Principle I (Defense in Depth), DoS protection
- **A.8.7 - Protection against malware**: Principle I, antivirus, EDR
- **A.8.8 - Technical vulnerabilities**: Principle XIV (Vulnerability Management)
- **A.8.9 - Configuration management**: Principle XV (Immutable Infrastructure)
- **A.8.10 - Information deletion**: Principle X (Audit), secure deletion
- **A.8.11 - Data masking**: Principle XII (Input Validation), tokenization
- **A.8.12 - Data leakage prevention**: Principle XIII (Secrets), DLP
- **A.8.16 - Monitoring activities**: Principle XVIII (Monitoring), SIEM
- **A.8.23 - Web filtering**: Principle I (Defense in Depth), proxy
- **A.8.24 - Cryptographic controls**: Principle VIII (Cryptographic Agility)
- **A.8.28 - Secure coding**: Principle IX (SDL), SAST
- **A.8.29 - Security testing**: Principle IX (SDL), DAST, pentesting
- **A.8.32 - Change management**: Principle XV (IaC), GitOps

### PCI-DSS v4.0

| PCI Requirement | Principles | Implementation |
|-----------------|------------|----------------|
| **1. Network Security** | I (Defense in Depth), VII (Zero Trust) | Firewalls, segmentation, microsegmentation |
| **2. Secure Configurations** | VI (Secure by Default) | CIS benchmarks, hardening |
| **3. Protect Stored Data** | VIII (Cryptographic Agility) | Encryption, tokenization, masking |
| **4. Protect Cardholder Data in Transit** | VIII (Cryptographic Agility) | TLS 1.2+, strong ciphers |
| **5. Protect Systems from Malware** | I (Defense in Depth) | Antivirus, EDR, sandboxing |
| **6. Develop Secure Systems** | IX (SDL) | Secure coding, code review, SAST |
| **7. Restrict Access** | II (Least Privilege) | RBAC, MFA, JIT access |
| **8. Identify Users** | VII (Zero Trust) | Unique IDs, MFA, strong auth |
| **9. Restrict Physical Access** | I (Defense in Depth) | Physical controls, surveillance |
| **10. Log and Monitor** | X (Audit Everything) | SIEM, audit logs, retention |
| **11. Test Security** | XIV (Vulnerability Management), IX (SDL) | Vulnerability scans, pentesting |
| **12. Support Information Security** | Organizational Enablement | Policies, training, incident response |

### GDPR

| GDPR Article | Principles | Implementation |
|--------------|------------|----------------|
| **Article 25 - Data Protection by Design** | IX (SDL), XVI (Threat Modeling) | Privacy-focused architecture, DPIA |
| **Article 30 - Records of Processing** | X (Audit Everything) | Data inventory, processing logs |
| **Article 32 - Security of Processing** | I-XVIII (all principles) | Encryption, access controls, pseudonymization |
| **Article 33 - Breach Notification** | XVIII (Incident Response) | IR plan, 72-hour notification |
| **Article 35 - Data Protection Impact Assessment** | XVI (Threat Modeling) | DPIA for high-risk processing |

---

## Metaprinciples

**Security is Not Optional Functionality.**  
Performance, usability, and feature velocity are negotiated with security, never at its expense. Security is a constraint, not a feature to be traded off.

**Defense in Depth Over Single Solutions.**  
No single control is sufficient. Layered security ensures resilience. Assume every layer will eventually fail; design for graceful degradation.

**Shift Left: Security Early, Not Late.**  
Integrate security in design phase, not as post-deployment bolt-on. Cost of fixing vulnerabilities increases exponentially through SDLC: $1 at design, $10 in dev, $100 in testing, $1000 in production, $10000 after breach.

**Assume Breach.**  
Design systems assuming attackers are already inside. Focus on detection, containment, and recovery as much as prevention. Zero Trust architecture embodies this principle.

**Secure by Default, Usable by Configuration.**  
Ship with maximal security enabled. Require conscious, documented decisions to relax constraints. Never optimize for convenience at expense of security in default state.

**Visibility is Foundation.**  
Cannot secure what you cannot see. Comprehensive logging, monitoring, and observability are prerequisites for security. MTTD (Mean Time To Detect) is as critical as MTTR (Mean Time To Respond).

**Automation Over Manual Processes.**  
Manual security processes don't scale and are error-prone. Automate security gates (SAST, DAST, SCA), policy enforcement (OPA), and incident response (SOAR). Free humans for strategic tasks.

**Simplicity Enables Security.**  
Complexity is the enemy of security. Simple systems are auditable, testable, and comprehensible. Economy of mechanism reduces attack surface and bug count.

**Fail Secure, Not Open.**  
System failures must default to secure state. Deny access on error, preserve audit logs, alert on anomalies. Availability is important but never at expense of security posture.

**Continuous Improvement.**  
Security posture degrades without active maintenance. Regular reassessment mandatory (threat modeling annually, access reviews quarterly, penetration testing annually). Threat landscape evolves; defenses must too.

**Shared Responsibility.**  
Security is everyone's responsibility; specialized expertise augments but does not replace developer/operator ownership. Embed security champions in product teams rather than centralize all security work.

**Measure to Improve.**  
What gets measured gets managed. Track security metrics (MTTD, MTTR, vulnerability SLA compliance, patch coverage). Use data to drive prioritization and demonstrate ROI.

**Blameless Culture.**  
Punishing individuals for security mistakes drives underreporting and fear. Focus on systemic improvements, not individual fault. Psychological safety enables proactive security reporting.

**Threat-Informed Defense.**  
Defenses must align with real-world threats. Use threat intelligence, MITRE ATT&CK, and incident learnings to prioritize controls. Don't build defenses for theoretical threats while ignoring active exploitation.

**Verify, Don't Trust.**  
"Trust but verify" is insufficient. Zero Trust principle: verify every request, regardless of source. Network location ≠ trustworthiness. Continuous authentication and authorization.

---

## Version History

**v2.0 (2025-11-20)**

Major expansion with comprehensive implementation guidance:

**New Principles:**
- Added Principle XVI: Threat Modeling
- Added Principle XVII: Supply Chain Security
- Added Principle XVIII: Security Monitoring & Incident Response

**Expanded Existing Principles:**
- Principle I (Defense in Depth): Added architecture patterns, layer strategies, technology stacks
- Principle VII (Zero Trust): Added implementation phases, device posture checking, continuous authentication
- Principle IX (SDL): Expanded from brief overview to full SDLC integration with tooling, CI/CD examples
- Principle X (Audit Everything): Added structured logging, tamper-evident logging, SIEM architecture, privacy considerations
- Principle XII (Input Validation): Added file upload validation, CSP, CORS, ReDoS prevention, defense-in-depth
- Principle XIII (Secrets Management): Added rotation strategies, break-glass procedures, secrets sprawl detection, tool comparison
- Principle XIV (Vulnerability Management): Added risk-based prioritization (EPSS), compensating controls, bug bounty programs, zero-day response
- Principle XV (Immutable Infrastructure): Added GitOps, image signing, supply chain security, incident response for compromised systems

**New Sections:**
- Trade-offs & Resolution Patterns (6 common conflicts with resolutions)
- Anti-Patterns (9 common security failures with consequences and solutions)
- Tool Ecosystem Map (comprehensive mapping of principles to open source and commercial tools)
- Implementation Checklists (actionable checklists for all 18 principles)
- Security Maturity Model (6 levels from Ad Hoc to Industry-Leading)
- Organizational Enablement (executive sponsorship, incentives, training, community, Conway's Law, change management)
- Learning Paths (30-day quickstart, 3-month deep dive, 1-day executive overview)
- Modern Architecture Considerations (cloud-native, microservices, serverless, containers, Kubernetes)
- Compliance Mapping (OWASP Top 10, NIST CSF, CIS Controls, ISO 27001, PCI-DSS, GDPR)
- Expanded Metaprinciples (15 foundational philosophies)
- Version History (this section)

**Content Statistics:**
- Principles: 15 → 18 (+3 new)
- Word count: ~3,000 → ~35,000 (+1100%)
- Code examples: ~10 → ~80+
- Practical checklists: 0 → 18
- Tool recommendations: ~20 → ~100+

**Acknowledgments:**
Built on industry standards (OWASP, NIST, CIS, ISO 27001), battle-tested practices from cloud providers (AWS, Azure, GCP), and lessons from major security incidents (SolarWinds, Log4Shell, Colonial Pipeline).

---

**v1.0 (2025-XX-XX)**

Initial release with 15 foundational principles covering core security concepts.

---

## References

**Standards & Frameworks:**
- OWASP Top 10: https://owasp.org/Top10/
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- CIS Controls v8: https://www.cisecurity.org/controls/
- ISO 27001:2022: https://www.iso.org/standard/27001
- PCI-DSS v4.0: https://www.pcisecuritystandards.org/
- MITRE ATT&CK: https://attack.mitre.org/

**Books:**
- "The Phoenix Project" (Gene Kim) - DevOps and security culture
- "Threat Modeling: Designing for Security" (Adam Shostack)
- "Security Engineering" (Ross Anderson)
- "Building Secure and Reliable Systems" (Google SRE)
- "Zero Trust Networks" (Evan Gilman, Doug Barth)

**Online Resources:**
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- PortSwigger Web Security Academy: https://portswigger.net/web-security
- Cloud Security Alliance: https://cloudsecurityalliance.org/
- SANS Reading Room: https://www.sans.org/reading-room/
- SLSA Framework: https://slsa.dev/

**Industry Reports:**
- Verizon Data Breach Investigations Report (annual)
- IBM Cost of a Data Breach Report (annual)
- SANS Security Survey Reports
- Gartner Market Guides (SIEM, CSPM, SOAR)

**Case Studies:**
- "How AWS Uses Formal Methods" (Amazon): https://lamport.azurewebsites.net/tla/amazon.html
- "Building Secure and Reliable Systems" (Google SRE): https://sre.google/books/
- "The SolarWinds Breach: What We Know" (Krebs on Security)

---

**Status**: Living document - community contributions welcome  
**Feedback**: GitHub Issues / Pull Requests  
**Citation**: "Security Hardening Manifesto v2.0" (2025), licensed under CC0 Public Domain  

---

**Acknowledgments**: Built on OWASP principles, NIST guidelines, CIS benchmarks, ISO 27001 standards, and real-world lessons from practitioners at cloud providers, financial institutions, and security-critical organizations. Special recognition to the open source security community for tooling and knowledge sharing.
