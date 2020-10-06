SHELL := /bin/bash
PWD := $(shell pwd)

GIT_REMOTE = github.com/7574-sistemas-distribuidos/docker-compose-init

default: build

all:

deps:
	go mod tidy
	go mod vendor

build: deps
	GOOS=linux go build -o bin/client github.com/7574-sistemas-distribuidos/docker-compose-init/client
.PHONY: build

docker-image:
	sudo docker build -f ./server/Dockerfile -t "server:latest" .
	sudo docker build -f ./client/Dockerfile -t "client:latest" .
.PHONY: docker-image

docker-compose-up: docker-image
	sudo docker-compose -f docker-compose-dev.yaml up -d --build
.PHONY: docker-compose-up

docker-compose-down:
	sudo docker-compose -f docker-compose-dev.yaml stop -t 1
	sudo docker-compose -f docker-compose-dev.yaml down
.PHONY: docker-compose-down

docker-compose-logs:
	sudo docker-compose -f docker-compose-dev.yaml logs -f
.PHONY: docker-compose-logs

net-test:
#	echo 1 | sudo docker run -i --network=7574-tp0_testing_net busybox nc server 12345
	diff <(echo 1 | sudo docker run -i --network=7574-tp0_testing_net busybox nc server 12345) <(echo "Your Message has been received: b'1'")
.PHONY: net-test

