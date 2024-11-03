run:
	docker run -p 55001:55001 lyra:latest

# build image
build:
	docker build . -t lyra:latest

# build and push
bdrn:
	make build
	make run

bdtest:
	docker build . -t ras334/lyra:dev
	docker login
	docker push ras334/lyra:dev
