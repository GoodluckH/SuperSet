.PHONY: prepare
prepare:
	@pip install -r requirements.txt
	@cp .env.example .env

.PHONY: install
install:
	@pip install -r requirements.txt

.PHONY: start
start:
	@streamlit run main.py