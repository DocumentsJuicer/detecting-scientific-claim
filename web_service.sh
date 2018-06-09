python -m allennlp.service.server_simple \
    --archive-path static_html/model.tar.gz \
    --predictor discourse \
    --include-package discourse \
    --title "Discourse Prediction" \
    --field-name sentences