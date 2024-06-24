from towhee import pipe, ops, DataCollection

p = (
    pipe.input('text')
        .map('text', 'vec', ops.text_embedding.dpr(model_name='facebook/dpr-ctx_encoder-single-nq-base'))
        .output('text', 'vec')
)

DataCollection(p('你好啊.')).show()