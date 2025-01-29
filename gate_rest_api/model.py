# -*- coding: utf-8 -*-
import mimetypes
import base64

from typing import Optional
from pydantic import BaseModel as PyBaseModel, Field, Base64Bytes, Base64Str


class BaseModel(PyBaseModel):
    class Config:
        arbitrary_types_allowed = True


class SecurityData(BaseModel):

    key: Optional[str]
    secret: Optional[str]


class Response(BaseModel):

    status: Optional[str] = Field(pattern=r"Success|NotSuccess")
    error: Optional[str] = Field(default=None)


class File(BaseModel):

    name: Optional[str] = None
    type: Optional[str] = None
    payload: Optional[Base64Str] = None

    def get_mime(self) -> str:
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            str: _description_
        """
        try:
            _type = self.type
            if "." == _type[0]:
                _type = _type[1:]
            return mimetypes.types_map[f".{_type}"]
        except KeyError:
            raise ValueError(f"mime type {self.type} not found in mimetypes.types_map")

    def encode_payload(self, payload: bytes, type_encode="utf-8") -> Base64Str:
        """_summary_

        Args:
            payload (bytes): _description_
            type_encode (str, optional): _description_. Defaults to "utf-8".

        Returns:
            str: _description_
        """
        _payload = payload
        if not isinstance(payload, bytes):
            _payload = payload.encode(type_encode)
        return base64.b64encode(_payload).decode(type_encode)

    def decode_payload(self, payload: Base64Str, type_encode="utf-8") -> Base64Bytes:
        """_summary_

        Args:
            payload (bytes): _description_
            type_encode (str, optional): _description_. Defaults to "utf-8".

        Returns:
            bytes: _description_
        """
        _payload = payload
        if not isinstance(payload, bytes):
            _payload = payload.encode(type_encode)
        return base64.b64decode(_payload)


class From(BaseModel):

    host: Optional[str] = Field(
        None,
        pattern=r"^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*"
        + r"([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])?$|"
        + r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]"
        + r"|[01]?[0-9][0-9]?)$",
    )
    port: Optional[str] = Field("25", pattern=r"^(\d{1,5})$")
    username: Optional[str] = Field(
        None, pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )
    password: Optional[str]


class SMTPBody(BaseModel):

    text: Optional[str] = Field(default=None)
    file: Optional[File] = Field(default=None)
    subject: Optional[str] = Field(default=None)
    to: Optional[str] = Field(
        None, pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )
    from_: Optional[From] = Field(default=None)

# class SMTPBodyWithFile(BaseModel):

#     text: Optional[str] = Field(default=None)
#     file: Optional[File] = Field(default=None)
#     subject: Optional[str] = Field(default=None)
#     to: Optional[str] = Field(
#         None, pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#     )
#     from_: Optional[From] = Field(default=None)
