run:
	docker run lyra:latest

# build image
build:
	docker build . -t lyra:latest

# build and push
bpsh:
	make build
	make run
