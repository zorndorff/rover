FROM node:alpine

WORKDIR /etc/app/
ADD package* ./
RUN npm install
ADD . .

CMD node bin/www