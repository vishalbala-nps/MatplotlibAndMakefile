current_dir := $(shell pwd)
all:dataplot
clean:
	rm -rf $(current_dir)/data.txt
	rm -rf $(current_dir)/datagen
dataplot: clean
	${CC} $(current_dir)/datagen.c -o $(current_dir)/datagen
	$(current_dir)/datagen > $(current_dir)/data.txt
	python3 $(current_dir)/graph.py

	
