luigi_mode=--local-scheduler

clean:
	rm -f ../logs/log.txt
	rm -f ../finished_file_token/*
	rm -f ../data/extracted/*.csv
	rm -f ../data/transformed/*.csv

ExtractQiitaItem:
	rm -f ../finished_file_token/$@
	rm -f ../logs/log.txt
	python run_workflow.py $@ $(luigi_mode)

TransformQiitaItem:
	rm -f ../finished_file_token/$@
	rm -f ../logs/log.txt
	python run_workflow.py $@ $(luigi_mode)

LoadQiitaItem:
	rm -f ../finished_file_token/$@
	rm -f ../logs/log.txt
	python run_workflow.py $@ $(luigi_mode)

ETLQiita:
	make clean
	make ExtractQiitaItem
	make TransformQiitaItem
	make LoadQiitaItem
