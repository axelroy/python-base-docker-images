#!/usr/bin/env bash
if groups $USER | grep &>/dev/null '\bdocker\b'; then
  CAPTAIN="captain"
else
  CAPTAIN="sudo captain"
fi

$CAPTAIN build
