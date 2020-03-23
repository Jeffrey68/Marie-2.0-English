from telegram import (TelegramObject)


class PollOption(TelegramObject):
    """
    This object contains information about one answer option in a poll.

    Attributes:
        text (:obj:`str`): Option text, 1-100 characters.
        voter_count (:obj:`int`): Number of users that voted for this option.

    Args:
        text (:obj:`str`): Option text, 1-100 characters.
        voter_count (:obj:`int`): Number of users that voted for this option.

    """

    def __init__(self, text, voter_count, **kwargs):
        self.text = text
        self.voter_count = voter_count

    @classmethod
    def de_json(cls, data, bot):
        if not data:
            return None

        return cls(**data)


class Poll(TelegramObject):
    """
    This object contains information about a poll.

    Attributes:
        id (:obj:`str`): Unique poll identifier.
        question (:obj:`str`): Poll question, 1-255 characters.
        options (List[:class:`PollOption`]): List of poll options.
        is_closed (:obj:`bool`): True, if the poll is closed.

    Args:
        id (:obj:`str`): Unique poll identifier.
        question (:obj:`str`): Poll question, 1-255 characters.
        options (List[:class:`PollOption`]): List of poll options.
        is_closed (:obj:`bool`): True, if the poll is closed.

    """

    def __init__(self, id, question, options, is_closed, **kwargs):
        self.id = id
        self.question = question
        self.options = options
        self.is_closed = is_closed

        self._id_attrs = (self.id,)

    @classmethod
    def de_json(cls, data, bot):
        if not data:
            return None

        data = super(Poll, cls).de_json(data, bot)

        data['options'] = [PollOption.de_json(option, bot) for option in data['options']]

        return cls(**data)

    def to_dict(self):
        data = super(Poll, self).to_dict()

        data['options'] = [x.to_dict() for x in self.options]

        return data

__mod_name__ = "Poll"

__help__ = """
 - 
"""
