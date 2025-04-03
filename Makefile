.PHONY: tag

VERSION = $(filter-out $@,$(MAKECMDGOALS))

tag:
	@echo "Updating version to $(VERSION)..."

	# 1. Update version in aichatcoder/__init__.py
	@sed -i "s/^__version__ = .*/__version__ = \"$(VERSION)\"/" aichatcoder/__init__.py

	# 2. Update version in pyproject.toml
	@sed -i "s/^version = .*/version = \"$(VERSION)\"/" pyproject.toml

	# 3. Commit the changes
	@git add .
	@git commit -m "updated for release $(VERSION)"
	@git push

	# 4. Create a new tag
	@git tag $(VERSION)

	# 5. Push the tag to origin
	@git push origin $(VERSION)

	@echo "Version $(VERSION) tagged and pushed successfully."
