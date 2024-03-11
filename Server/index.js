const express = require('express');
const cors = require('cors');
const ytdl = require('ytdl-core');
const path = require('path')
const app = express();
const PORT = 4000;

app.use(cors());

app.use(express.static('../'));

app.listen(PORT, () => {
	console.log(`Server Works !!! At port ${PORT}`);
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/downloadmp3', async (req, res, next) => {
  try {
    var url = req.query.url;
    if(!ytdl.validateURL(url)) {
        return res.sendStatus(400);
    }
    let title = 'audio';

    let info = await ytdl.getBasicInfo(url, { format: 'mp4' });
    console.log(indo)

    title = info.player_response.videoDetails.title.replace(/[^\x00-\x7F]/g, "");

    res.header('Content-Disposition', `attachment; filename="${title}.mp3"`);
    ytdl(url, {
        format: 'mp3',
        filter: 'audioonly',
    }).pipe(res);

  } catch (err) {
      console.error(err.message);
  }
});

app.get('/downloadmp4', async (req, res, next) => {
  try {
    let url = req.query.url;
    if(!ytdl.validateURL(url)) {
        return res.sendStatus(400);
    }
    let title = 'video';

    let info = await ytdl.getBasicInfo(url, { format: 'mp4' });
    console.log(indo)
    title = info.player_response.videoDetails.title.replace(/[^\x00-\x7F]/g, "");

    res.header('Content-Disposition', `attachment; filename="${title}.mp4"`);
    ytdl(url, {
        format: 'mp4',
    }).pipe(res);

  } catch (err) {
      console.error(err);
  }
});