SPECS := $(shell for f in */SPECS/*.spec; do [[ $$f == rpmbuild* ]] && continue; f=$${f%.spec}; echo $${f\#\#*/}; done)

all:
	@echo -e "Please choose one of the following target:\n  init\n  clean"
	@for s in $(SPECS); do \
		printf "  %s\n" $$s; \
	done
	@exit

init:
	yum install -y rpm-build rpmdevtools

clean:
	rm -rf ~/rpmbuild/

.PHONY: $(SPECS)

$(SPECS):
	$(eval spec := $@)
	@# in case we store several specs in one folder like this foo/SPECS/foo-bar.spec
	$(eval dir := $(shell echo $@ | cut -d "-" -f1))
	mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS,tmp}
	cp -r $(dir)/* ~/rpmbuild/
	@WGETRC=`pwd`/.wgetrc spectool --get-files --directory ~/rpmbuild/SOURCES/ ~/rpmbuild/SPECS/$(spec).spec
	rpmbuild --define "_tmppath %{_topdir}/tmp" -bb ~/rpmbuild/SPECS/$(spec).spec
