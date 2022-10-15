# Q & A

## create some artists

- drake=Artist(Stage_name='drake', Social_link='https://www.instagram.com/drake/') drake.save()

- hamza = Artist(Stage_name='Hamza Namira', Social_link='https://www.instagram.com/hamzanamira/') hamza.save()

- fouad = Artist(Stage_name='Mohamed Fouad', Social_link='https://www.instagram.com/mohamedfouadofficial/') fouad.save()

- tamer = Artist(Stage_name='Tamer Hossni', Social_link='https://www.instagram.com/Tamerhosny/') tamer.save()

- medhat = Artist(Stage_name='Medhat Saleh', Social_link='https://www.instagram.com/official.medhat.saleh/') medhat.save()

- ahmed = Artist.objects.create(Stage_name='Ahmed Al Hosani', Social_link='https://www.instagram.com/singerahmedalhosani/') ahmed.save()

## list down all artists

- list(Artist.objects.all())
- [<Artist: Ahmed Al Hosani>, <Artist: Hamza Namira>, <Artist: Medhat Saleh>, <Artist: Mohamed Fouad>, <Artist: Tamer Hossni>, <Artist: drake>]
## list down all artists sorted by name

- list(Artist.objects.all().order_by('Stage_name')) 
- [<Artist: Ahmed Al Hosani>, <Artist: Hamza Namira>, <Artist: Medhat Saleh>, <Artist: Mohamed Fouad>, <Artist: Tamer Hossni>, <Artist: drake>]

## list down all artists whose name starts with a

- list(Artist.objects.all().filter(Stage_name__startswith='a')) 
- [<Artist: Ahmed Al Hosani>]

## in 2 different ways, create some albums and assign them to any artists (hint: use objects manager and use the related object reference)

#### First way:

- Insan = Album(artist = Artist.objects.all().filter(Stage_name='Hamza Namira')[0], name = 'Insan', release_at='2022-10-15', cost=1232.5) Insan.save()
- Fakra = Album(artist = Artist.objects.all().filter(Stage_name='Hamza Namira')[0], name = 'Fakra', release_at='2021-01-01', cost=1232.5) Fakra.save()
- ala_allah = Album(artist = Artist.objects.all().filter(Stage_name='Hamza Namira')[0], name = 'ala allah', release_at='2022-10-14', cost=3242.5) ala_allah.save()

#### Second way:

- hamza = Artist.objects.all().filter(Stage_name='Hamza Namira')[0]
- hamza.albums.create(artist = hamza, name = 'Insan', release_at='2022-10-15'', cost=1232.5)
- hamza.albums.create(artist = hamza, name = 'Fakra', release_at='2021-01-01', cost=1232.5)
- hamza.albums.create(artist = hamza, name = 'ala allah', release_at='2022-10-14', cost=3242.5)

## get the latest released album

- Album.objects.all().order_by('-release_at')[0]
- <Album: Insan>

## get all albums released before today

- list(Album.objects.all().filter(release_at__lt=datetime.now().date()))
- [<Album: Fakra>, <Album: ala allah>]

## get all albums released today or before but not after today

- list(Album.objects.all().filter(~Q(release_at=datetime.now().date())))
- [<Album: Fakra>, <Album: ala allah>]

## count the total number of albums

- Album.objects.all().count() 
- 3

## in 2 different ways, for each artist, list down all of his/her albums

#### first way:

- Artist.objects.get(Stage_name='Hamza Namira').albums.values()

#### second way:

- list(Album.objects.all().filter(artist=Artist.objects.all().get(Stage_name='Hamza Namira')))
- [<Album: Insan>, <Album: Fakra>, <Album: ala allah>]
- 
## list down all albums ordered by cost then by name

- Album.objects.all().order_by('cost','name')
- [<Album: Fakra>, <Album: Insan>, <Album: ala allah>]
