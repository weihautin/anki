all:
	bzr merge
	./update-pot.sh
	./update-mos.sh
	bzr commit -m update
	bzr push
	cp -av qt48/* ../dtop/locale/
