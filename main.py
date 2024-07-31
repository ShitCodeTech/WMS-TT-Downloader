import requests

cookies = {
    'uid': '3aff7c4b3c719905',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/json',
    'Origin': 'https://sssinstagram.com',
    'Connection': 'keep-alive',
    # 'Cookie': 'uid=3aff7c4b3c719905',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    'url': 'https://www.instagram.com/reel/C9PvVo-J9OM/?igsh=MW84czNndmJlYzMzYQ==',
    'ts': 1721735413452,
    '_ts': 1721207406718,
    '_tsc': 0,
    '_s': '0fb66a287768ebc7c590fa9bee30f1e6a31dc023c549775ddfeb1ab9b499b778',
}

response = requests.post('https://sssinstagram.com/api/convert', cookies=cookies, headers=headers, json=json_data)

print(response.content)






C84791B91DA75EA0D281B797D5A7D7A9




b'{"url":[{"url":"https:\\/\\/media.sssinstagram.com\\/get?__sig=G4Ss3j8UEB9HCBIKVAdLug&__expires=1721737491&uri=https%3A%2F%2Finstagram.fcmn1-4.fna.fbcdn.net%2Fo1%2Fv%2Ft16%2Ff1%2Fm86%2FC84791B91DA75EA0D281B797D5A7D7A9_video_dashinit.mp4%3Fefg%3DeyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uY2xpcHMuYzIuNzIwLmJhc2VsaW5lIn0%26_nc_ht%3Dinstagram.fcmn1-4.fna.fbcdn.net%26_nc_cat%3D106%26vs%3D1126284341793751_1277425915%26_nc_vs%3DHBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9DODQ3OTFCOTFEQTc1RUEwRDI4MUI3OTdENUE3RDdBOV92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dGS0p6UnJONlVkcEdHVUJBSS1rSlNVaXkteHlicV9FQUFBRhUCAsgBACgAGAAbABUAACbw1Pq37tWSQBUCKAJDMywXQB5DlYEGJN0YEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HAA%253D%253D%26_nc_rid%3D8448e69468%26ccb%3D9-4%26oh%3D00_AYAUBN52aPq_C9HhRru3oA_qw1WZ_oYO0KMwOHvYihfWPw%26oe%3D66A09FE0%26_nc_sid%3D2999b8%26dl%3D1&filename=C84791B91DA75EA0D281B797D5A7D7A9_video_dashinit.mp4&ua=-&referer=https%3A%2F%2Fwww.instagram.com%2F","name":"MP4","type":"mp4","ext":"mp4"}],"thumb":"https:\\/\\/media.sssinstagram.com\\/get?__sig=3WyENT5guF7fQjgoPyn75w&__expires=1721737491&uri=https%3A%2F%2Finstagram.fcmn1-1.fna.fbcdn.net%2Fv%2Ft51.29350-15%2F450542917_461762413140302_2509925354897638925_n.jpg%3Fstp%3Ddst-jpg_e35_p1080x1080_sh0.08%26_nc_ht%3Dinstagram.fcmn1-1.fna.fbcdn.net%26_nc_cat%3D102%26_nc_ohc%3D-RzTdylhqn8Q7kNvgHJuR4X%26edm%3DAP_V10EBAAAA%26ccb%3D7-5%26oh%3D00_AYDTlbu_m1-vSNI5NFKpDj8dWXs-yuo-vdHAD12TC5nDGw%26oe%3D66A469C2%26_nc_sid%3D2999b8","sd":null,"meta":{"title":"C84791B91DA75EA0D281B797D5A7D7A9_video_dashinit.mp4","source":"https:\\/\\/www.instagram.com\\/p\\/C9PvVo-J9OM\\/","shortcode":"C9PvVo-J9OM","comments":[{"text":"This is Snoop Dogg, he can do anything","username":"eimjsi"},{"text":"\\ud83d\\udd25","username":"rebeccacrudden"},{"text":"WHAT-","username":"ana_.rangell"},{"text":"Sarehat wa","username":"iamlutfimaulana"},{"text":"Snoop Chicha","username":"btmathdeymayankkk"},{"text":"\\ud83d\\ude02\\ud83d\\ude02","username":"malak___shy"},{"text":"kurang2 in gele kawan","username":"ymqja"},{"text":"Switch your phone off \\ud83d\\ude2d\\ud83d\\udc94","username":"iqrahateseveryone"},{"text":"Unc what r doinnn","username":"supercrispyfriedchicken"}],"comment_count":2210,"like_count":160934,"taken_at":1720622576},"hosting":"instagram.com","hd":null,"timestamp":1721733553}'