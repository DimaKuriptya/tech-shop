# Tech Shop
## Overview
This is an online shop project. It was created by using such technologies as:
- Python
- Django
- PostgreSQL
- Celery
- Redis
- HTML / CSS + Bootstrap
- Docker / Docker Compose
- Pytest
## Running with Docker
First of all create project folder and select it:
```
mkdir proj_folder
```
```
cd proj_folder

```
Then clone the repository:
```
git clone https://github.com/DimaKuriptya/tech-shop.git
```
Create .env file. Set the following fields:

- `SECRET_KEY` - secures HTTP sessions, set to a random value.
- `EMAIL_HOST` - the SMTP server.
- `EMAIL_HOST_USER` - the SMTP username.
- `EMAIL_HOST_PASSWORD` - the SMTP password.
- `STRIPE_PUBLISHABLE_KEY` - the value you can get by creating a Stripe account.
- `STRIPE_SECRET_KEY` - the value you can get by creating a Stripe account.
- `STRIPE_WEBHOOK_SECRET` - the value you can get by creating a Stripe account
- `POSTGRES_HOST`=postgres
- `POSTGRES_PORT`=5432
- `POSTGRES_DB`=tech_shop
- `POSTGRES_USER`=postgres
- `POSTGRES_PASSWORD`=123
- `REDIS_URL`=redis://redis:6379

Create and start containers:
```
docker-compose up
```
After building you will be able to access the project at http://localhost:8000 URL.
## Gallery
### Here you can see the main pages of the project <br />
Goods browsing page: <br />
![goods_page](https://github.com/DimaKuriptya/tech-shop/assets/52717909/ddda592d-b96a-4653-ab24-34c47abc77a6)
Modal cart on the goods browsing page: <br />
![cart_modal](https://github.com/DimaKuriptya/tech-shop/assets/52717909/9026bc36-47b0-4d7b-bd83-8e095508c407)
Product details page: <br />
![product_details](https://github.com/DimaKuriptya/tech-shop/assets/52717909/03414e61-287f-4018-a40e-c6acfb355525)
Profile page: <br />
![profile](https://github.com/DimaKuriptya/tech-shop/assets/52717909/389275c1-fb4b-4404-a84c-3658e1fd8e99)
Orders list on the profile page: <br />
![orders](https://github.com/DimaKuriptya/tech-shop/assets/52717909/ef5e122e-d841-4ea5-8634-0814fe1e2a22)
