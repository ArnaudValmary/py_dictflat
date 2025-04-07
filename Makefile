
deps_groups := $(shell \
	cat pyproject.toml \
	| grep -E '^\[tool\.poetry\.group\.[^].]+\.dependencies\]' \
	| cut -d . -f 4 \
	| tr "\n" " " \
)

poetry_opt_groups = $(patsubst %,--with %, $(deps_groups))

poetry_version        := $(shell poetry --version)
poetry_python_version_msg := $(shell poetry run python --version  2>&1 >/dev/null)
poetry_python_version := $(shell poetry run python --version 2>/dev/null)
poetry_env_path       := $(shell poetry env info --path)

doc:
	@echo -n
	@echo "Poetry     : $(poetry_version)"
	@echo "• groups   : $(deps_groups)"
	@echo "• env path : $(poetry_env_path)"
	@echo "• Python   : $(poetry_python_version)"
	@if [[ -n "$(poetry_python_version_msg)" ]]; then \
		echo "• Message  : $(poetry_python_version_msg)"; \
	fi
	@echo
	@echo "Targets"
	@echo "• Dependencies"
	@echo "  → deps       : Install default dependencies"
	@echo "  → deps_all   : Install all dependencies"
	@echo "  → deps_clean : Clean Poetry all dependencies cache and lock file"
	@echo "  → deps_show  : Show installed dependencies tree"
	@echo "• Test"
	@echo "  → test       : Run test"
	@echo "  → test_clean : Clean all test cache directories"
	@echo "• Misc"
	@echo "  → clean      : Call all '*_clean' targets"
	@echo "  → force      : Call 'clean', 'deps_all' and 'test' targets"
	@echo

deps_clean:
	poetry env remove --all
	# rm -rf "$(poetry_env_path)"
	rm -f poetry.lock

deps: deps_clean
	poetry install

deps_all: deps_clean
	poetry install $(poetry_opt_groups)

deps_show:
	poetry show --tree

deps_show_all:
	poetry show --tree $(poetry_opt_groups)

test_clean:
	find . -name "__pycache__" -exec rm -rf "{}" \; ; true

test: test_clean
	poetry run pytest --verbose -vv

clean: deps_clean test_clean

force: clean deps_all test
