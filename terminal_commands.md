# for running rabbitmq on docker

`docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management`

# for Stripe webhook listening to localhost

`stripe listen --forward-to localhost:8000/payment/webhook/`

# celery worker

`celery -A myshop worker -l info`

# celery flower

`celery -A myshop flower`

# run redis docker container

`docker run -it --rm --name redis -p 6379:6379 redis`
