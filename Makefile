run:
	@uv sync
	@source .venv/bin/activate.fish
	@fastapi run main.py --reload
