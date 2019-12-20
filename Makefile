all: py js

py: *.proto
	mkdir -p build/py
	pip install grpcio-tools
	protoc -I=. --python_out=build/py solar-production.proto

js: *.proto
	mkdir -p build/js
	protoc -I=. --js_out=import_style=commonjs:build/js solar-production.proto

golang: *.proto
	mkdir -p build/go
	protoc -I=. --go_out=build/go solar-production.proto

java: *.proto
	mkdir -p build/java
	protoc -I=. --java_out=build/java solar-production.proto

clean: 
	rm -rf build

.PHONY: py js clean

export:
	export PYTHONPATH=/Users/abhishek/Documents/SoketLabs/projects/protocols/mesh-solar-production/py:/Users/abhishek/Documents/SoketLabs/projects/cross-lang-mesh-rpc/py