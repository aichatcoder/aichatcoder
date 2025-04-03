.PHONY: release tag
.SILENT: release tag

# Helper function to increment the version patch number
increment_patch = $(shell echo $(1) | awk -F. '{print $$1"."$$2"."$$(NF)+1}')

release:
	@echo "Reading version from aichatcoder/__init__.py..."
	current_version=$(shell grep -Po '(?<=^__version__ = ")([0-9]+\.[0-9]+\.[0-9]+)' aichatcoder/__init__.py); \
	echo "Last version found: $$current_version"; \
	new_version=$$(echo $$current_version | awk -F. '{print $$1"."$$2"."$$(NF)+1}'); \
	echo "Auto-incremented patch version: $$new_version"; \
	read -p "Do you want to proceed with version $$new_version? (y/n): " confirm && if [ "$$confirm" != "y" ]; then exit 1; fi; \
	echo "Releasing version $$new_version..."; \
	sed -i "s/^__version__ = .*/__version__ = \"$$new_version\"/" aichatcoder/__init__.py; \
	sed -i "s/^version = .*/version = \"$$new_version\"/" pyproject.toml; \
	git add .; \
	git commit -m "updated for release $$new_version"; \
	git push; \
	echo "Version $$new_version released successfully."; \
	make -s tag

tag:
	@echo "Reading version from aichatcoder/__init__.py..."
	current_version=$(shell grep -Po '(?<=^__version__ = ")([0-9]+\.[0-9]+\.[0-9]+)' aichatcoder/__init__.py); \
	tag="v$$current_version"; \
	if git rev-parse "$$tag" >/dev/null 2>&1; then \
		echo "Tag $$tag already exists! Aborting."; \
		exit 1; \
	fi; \
	read -p "Do you want to create a tag for version $$tag? (y/n): " TAG_CONFIRM && if [ "$$TAG_CONFIRM" != "y" ]; then exit 1; fi; \
	echo "Tagging version $$tag..."; \
	git tag $$tag; \
	git push origin $$tag; \
	echo "Version $$tag tagged and pushed successfully."
