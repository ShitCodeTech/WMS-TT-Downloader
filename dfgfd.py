import pyktok as pyk
pyk.specify_browser('firefox')

pyk.save_tiktok('https://www.tiktok.com/@tiktok/video/7106594312292453675?is_copy_url=1&is_from_webapp=v1',
        True,
        'video_data.csv',
		'firefox'
        )