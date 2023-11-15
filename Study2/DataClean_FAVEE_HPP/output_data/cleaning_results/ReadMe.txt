# When using the "{region}_dim_rel.csv"/"{region}_dim_rel_scaled.csv", 
# some dimension in certain regions should be reversed, 
# due to the bipolar in questionnaire is reversed.

raw_df = pd.read_csv('{region}_dim_rel.csv')
raw_scaled_df = pd.read_csv('{region}_dim_rel_scaled.csv')

if (region %in% c('Chile','Mexico','Spain')){
    raw_df['Goods.Exchange'] = 100-raw_df['Goods.Exchange']
    raw_scaled_df['Goods.Exchange'] = -raw_scaled_df['Goods.Exchange']}
if (region %in% c('Israel')){
    raw_df['Socioemotional'] = 100-raw_df['Socioemotional']
    raw_df['Synchronicity'] = 100-raw_df['Synchronicity']
    raw_scaled_df['Socioemotional'] = -raw_scaled_df['Socioemotional']
    raw_scaled_df['Synchronicity'] = -raw_scaled_df['Synchronicity']}
if (region %in% c('Brazil','Portugal','Russia')){
    raw_df['Morality'] = 100-raw_df['Morality']
    raw_scaled_df['Morality'] = -raw_scaled_df['Morality']}
if (region %in% c('France')){
    raw_df['Formality.and.Regulation'] = 100-raw_df['Formality.and.Regulation']
    raw_df['Expected.Reciprocity'] = 100-raw_df['Expected.Reciprocity']
    raw_df['Information.Exchange'] = 100-raw_df['Information.Exchange']
    raw_df['Money.Exchange'] = 100-raw_df['Money.Exchange']
    raw_df['Mating'] = 100-raw_df['Mating']
    raw_df['Importance.for.society'] = 100-raw_df['Importance.for.society']
    raw_df['Importance.for.individuals'] = 100-raw_df['Importance.for.individuals']
    raw_df['Occupational'] = 100-raw_df['Occupational']
    raw_scaled_df['Formality.and.Regulation'] = -raw_scaled_df['Formality.and.Regulation']
    raw_scaled_df['Expected.Reciprocity'] = -raw_scaled_df['Expected.Reciprocity']
    raw_scaled_df['Information.Exchange'] = -raw_scaled_df['Information.Exchange']
    raw_scaled_df['Money.Exchange'] = -raw_scaled_df['Money.Exchange']
    raw_scaled_df['Mating'] = -raw_scaled_df['Mating']
    raw_scaled_df['Importance.for.society'] = -raw_scaled_df['Importance.for.society']
    raw_scaled_df['Importance.for.individuals'] = -raw_scaled_df['Importance.for.individuals']
    raw_scaled_df['Occupational'] = -raw_scaled_df['Occupational']}