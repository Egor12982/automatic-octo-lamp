time = int(input('Type time in seconds: '))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')