#!/usr/bin/env bash

download () {
  source "$WORKING_PATH/../.env"
  url="https://plex.tv/downloads/latest/5?channel=8&build=linux-x86_64&distro=debian&X-Plex-Token=$PLEX_TOKEN"
  redirect_url=$(curl -Ls -w %{url_effective} -o /dev/null "$url")
  file_name=${redirect_url#*debian\/}
  FILE_PATH=$(echo "$WORKING_PATH/../debs/$file_name")
  curl $redirect_url -o $FILE_PATH
}

install_package () {
  sudo apt install ./$FILE_PATH
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  WORKING_PATH=$(cd "$(dirname ${BASH_SOURCE[0]})"; pwd)
  download
  if [[ $1 == "install" ]]; then
    install_package
  fi
fi

