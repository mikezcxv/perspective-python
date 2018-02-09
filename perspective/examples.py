
def line(dat, col, index='index', key='key'):
    from .psp import psp
    return psp(dat,
               view='line',
               columns=[index, col],
               rowpivots=[index],
               columnpivots=[key],
               aggregates={index: 'last', col: 'last'})
