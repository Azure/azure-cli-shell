FROM azuresdk/azure-cli-python

WORKDIR . /.
COPY . .

RUN /bin/bash -c 'TMP_PKG_DIR=$(mktemp -d); \
python setup.py bdist_wheel -d $TMP_PKG_DIR;\
pip install azure-cli-shell -f $TMP_PKG_DIR;'

WORKDIR /

CMD bash