# for running rabbitmq on docker
`docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management`

# for Stripe webhook listening to localhost
`stripe listen --forward-to localhost:8000/payment/webhook/`
