from node:alpine

ADD package* .
RUN npm install
ADD . .

CMD node bin/www