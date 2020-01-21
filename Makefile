current_dir := $(shell pwd)
clean:
	rm $(current_dir)/data.txt
	rm $(current_dir)/datagen
dataplot:
	${CC} $(current_dir)/datagen.c -o $(current_dir)/datagen
	$(current_dir)/datagen > $(current_dir)/data.txt
	python3 $(current_dir)/graph.py

	