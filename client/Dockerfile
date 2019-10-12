from node:alpine as build

WORKDIR /etc/app/
ADD package* ./
RUN npm install
ADD . .

RUN npm run build

from nginx:stable-alpine as prod

COPY --from=build /etc/app/ .