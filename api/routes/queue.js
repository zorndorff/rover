const { Router } = require('express');
var router = Router();

/* GET users listing. */
router.get('/', async function(req, res, next) {
  res.send('respond with a resource');
});

module.exports = router;
