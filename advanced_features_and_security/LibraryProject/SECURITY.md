# Security Configuration for Advanced Features and Security Project

This document describes the security measures implemented in the Django project to enforce HTTPS, secure cookies, and add protection against common attacks.

---

## 1. Django Security Settings

The following settings are configured in `LibraryProject/settings.py`:

```python
# Enforce HTTPS
SECURE_SSL_REDIRECT = True  
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Security headers
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
