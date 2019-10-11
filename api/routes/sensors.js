const { Router } = require('express');
const { get } = require('../lib/cache');

const router = Router();

/* GET sensor listing. */
router.get('/', async (req, res, next) => {
  res.send('respond with a resource');
});

/* GET sensor by key. */
router.get('/:key', async (req, res, next) => {
  const value = await get(req.params.key);

  res.json({
    value
  });
});

module.exports = router;
