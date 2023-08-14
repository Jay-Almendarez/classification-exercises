from sklearn.model_selection import train_test_split

def ttv(df, target):
    '''
    ttv will take in a DataFrame and return train, validate, and test DataFrames; stratify on whatever you decide as the target in bracketed and quotations.
    For example: ttv(df,['survived']) will return the dataframe (in this case the titanic dataframe and stratify by 'survived').
    return train, validate, test DataFrames.
    '''
    train, test = train_test_split(df, test_size=.2, random_state=117, stratify=df[target])
    train, validate = train_test_split(train, test_size=.3, random_state=117, stratify=train[target])
    return train, validate, test