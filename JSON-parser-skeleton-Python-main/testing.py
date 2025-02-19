print(0e0021)
#prefix(e|E)suffix
#suffix can't be a decimal
#suffix can be 00023 or 0000
#prefix can have either a single zero with dot or not but cannot start with a zero and then have non zero
#in prefix after dot you can have multiple zeros as part of the fraction
pattern = "^[1-9][0-9]*(e|E)[0-9]+||||$"