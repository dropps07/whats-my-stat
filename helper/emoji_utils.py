import emoji
from collections import Counter
import pandas as pd

def emoji_helper(selected_user,df): #df= dataframe
    if selected_user!="Overall": #not overall means selected a specific person
        df=df[df['user']==selected_user] #shrink down to show only specific users msg
    emojis= []
    for msg in df['message']: #going thru spreadsheets 'message' col 
        emojis.extend([c for c in msg if emoji.is_emoji(c)]) #if its an emoji 'c' then take everything we find '.extend' and store it in emojis[].
    
    return pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))), columns=['emoji', 'count'])