import json

employee = """{"type": "service_account",
  "project_id": "python-pr-342609",
  "private_key_id": "0fa86526d1e0c80babc26437ae9cf0219eb107df",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC+WwghkOOUHzgN\nSNi64EVVdP1c4uww92+4Zi7DjKWDXyd6jPFaz0tuhEWIDJheyfIUhBUiEcg8DNFH\ncPQ6w2pPjcf97b6GJR3cCxtOYI7Po2YwV99g22doKpqCowjAflWchv6X1R/ibcen\nLNFtdhw1u8jmCfjtk3ewYrW5umZSJhjY/G3u78glqFt4D8GQA2yid6kFWHbUBmHS\n5Gf4qzAZ1GBdu/q9PeDyiidG4zwVb+ARSR0xHQ3p4y66Yj8YeDbrYL3FQxA9WC4L\nDuwgt12C/bGtxpGfrqohgNoIcCERKElSUyDPupBb6eQxJXFIx66JnNn0eumxPnCL\nY/hWNvuDAgMBAAECggEAV4XZjj1lNjTIe+szo3D80BcTa4L24GjUmG97LvRbIbU9\nnK5zRrKrVyxAIBbSdDrcMKyuXtTYQSwPiY6Y7O/u0Jc7Djki8eDdAtCkhHwHDddu\nY+nzTkBzIkT8d/ZoTsGHsYmsQ7l9iIm7U9Vakb7Np7Mo4wRQzUORs6sfLT9UTo5j\ndiCA/km0tjp48c8JlU76alcko6oBwZPTFHu90dMgcvzsGQVkhGjmAb7XQW7PoGQ1\n5dYs5ac+Bcwai0//8gSqeKPAiepjVv5YhovRNkoorY15rgl3rXm+BDMCs32Xjc/Z\nslLjeoT+/1akRz5pd8Lk94NQyi+t09E9TOfYORTUSQKBgQD26hH7nw9+WqGbkir7\nNA5GoXG76AlRmbS/wOR0EMXOXIKGrAXIEBM7PK4USL5v8qqdJbuKKMEJo0mPnDVO\nAE0FWQuhsGzkO1jruegRIegjxmou38im68RhK4Cs3mn16p8OJidEx/cery8YNdyH\nXhG8Ar3WwWyY+Nl4Trk8F9U0TQKBgQDFXC3MlrlccQ4/82s9r7qH2rp58ubbhd2t\nuUfzc2U2u8U2W1/iyOsc95VdXrjRI1dVX1B79+by+m9yNvhENRdefFF7A8t/yfIC\niE2BGg1LkCAlcywCG91XiBEGMLUro80fzErwNmrqLtXeBNP9g87gP8tB6y/j3G62\nlMqRSB4XDwKBgQDA24EiTVH3umiiL+Ach8NizbUdNRcaQnlYkRyfv34ROlbFQ9Xc\nNxoeWb4Kn+sHW76BsjgyqLRmh8DsR/GmtDt0ouGf8EKNXgGNVY762sYMM206oZaD\nMoIX97ewzqRq7VBA5/IiGiJeOC0Ltv5CSWqGtIl9FWVycmTCQJMUafUgvQKBgCcc\nyYbOKBYF4ckSuKIU/WaHFoWsecvvj6sqGPRKXjimpcLMAQi0wMOQ3W0PpJjt5BTr\nOswWqRJmR0ffVPxPeT4kbRFwAxhkMS4HTTTUsOXUvkottP8F/qumL5mGdaEcaT5w\nAjnwzudyOLgzRL/tK0aN3f5GWctSmC5e9nYsUKpJAoGASwJmdJ9NGf2po1nfOFrJ\nwUXD/rbBXIqDaOHNRHs/pSzAojf5jOj8Eg9+cPNxPsmV5SMjbBU1lAmWyJCYJzvO\nHkyFMA9GSFGAlDNTuYdt77InRglY2pncHy770Ey3WuoHS2pPYE8WL85bgIHvUr3T\n9rVs5XFbLTNEI4XvLCXrtac=\n-----END PRIVATE KEY-----\n",
  "client_email": "service-account@python-pr-342609.iam.gserviceaccount.com",
  "client_id": "110632577635186306018",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/service-account%40python-pr-342609.iam.gserviceaccount.com"}"""

# Convert string to Python dict
employee_dict = json.loads(employee, strict=False)
print(employee_dict)
