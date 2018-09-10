import pandas as pd

df = pd.read_csv('/Users/jonesgd/projects/hackathon/data/articles.A-B.xml.tar.gz.csv')
df2 = pd.read_csv('/Users/jonesgd/projects/hackathon/data/articles.C-H.xml.tar.gz.csv')
df3 = pd.read_csv('/Users/jonesgd/projects/hackathon/data/articles.I-N.xml.tar.gz.csv')
df4 = pd.read_csv('/Users/jonesgd/projects/hackathon/data/articles.O-Z.xml.tar.gz.csv')

#Add a column to show whether an Acknowledgment_Tag is present
df['ack_present'] = df.Acknowledgment_Tag.isna()

print(df)

#Reduce the file complexity by dropping the Acknowledgment_Tag
df = df.drop(labels={'Acknowledgment_Tag'}, axis=1)

print(df)

#Export to a CSV file

df.to_csv('articles.A-B.xml.tar.gz_reduced.csv')

df2['ack_present'] = df2.Acknowledgment_Tag.isna()
df2 = df2.drop(labels={'Acknowledgment_Tag'}, axis=1)
df2.to_csv('articles.C-H.xml.tar.gz_reduced.csv')

df3['ack_present'] = df3.Acknowledgment_Tag.isna()
df3 = df3.drop(labels={'Acknowledgment_Tag'}, axis=1)
df3.to_csv('articles.I-N.xml.tar.gz_reduced.csv')

df4['ack_present'] = df4.Acknowledgment_Tag.isna()
df4 = df4.drop(labels={'Acknowledgment_Tag'}, axis=1)
df4.to_csv('articles.O-Z.xml.tar.gz_reduced.csv')


print(df.ack_present.value_counts())

print(df2.ack_present.value_counts())

print(df3.ack_present.value_counts())

print(df4.ack_present.value_counts())


print(list(df))

print(list(df2))

print(list(df3))

print(list(df4))

exit()
