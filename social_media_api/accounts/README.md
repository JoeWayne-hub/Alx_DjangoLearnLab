# Social Media API

This is a Django REST Framework–based Social Media API that provides user authentication and profile management features. It serves as the foundation for building a complete social networking platform.

---

## 🚀 Features

- User registration with token authentication  
- User login and token generation  
- Custom user model with:
  - Profile picture  
  - Bio  
  - Followers system (ManyToMany relationship)  
- Secure API endpoints using Django REST Framework  

---

## 🛠️ Tech Stack

- Python 3.x  
- Django  
- Django REST Framework  
- Django REST Framework Authtoken  

---

## ⚙️ Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
POST /api/posts/
Headers: Authorization: Token <token>
Body: { "title": "Hello", "content": "..." }
### Follow / Feed APIs

- Follow/unfollow user:
  POST /api/accounts/follow/<user_id>/  (follow)
  DELETE /api/accounts/follow/<user_id>/  (unfollow)
  Requires Authentication

- List following:
  GET /api/accounts/following/

- List followers:
  GET /api/accounts/followers/

- Feed:
  GET /api/posts/feed/
  Returns posts from users you follow ordered by created_at desc.
### Likes
- POST /api/posts/<pk>/like/ — like a post (auth)
- POST /api/posts/<pk>/unlike/ — unlike a post (auth)

### Notifications
- GET /api/notifications/ — list notifications (auth)
- POST /api/notifications/<id>/mark-read/ — mark as read (auth)
