# -*- coding: utf-8 -*-

class List:
    def __init__(self, event_data: dict):
        self.list_id: str = event_data.get('id')
        self.server_id: str = event_data.get('serverId')
        self.channel_id: str = event_data.get('channelId')
        self.messages: dict = event_data.get('messages')
        self.created_at: str = event_data.get('createdAt')
        self.created_by: str = event_data.get('createdBy')
        self.created_by_webhook_id: str = event_data.get('createdByWebhookId')
        self.updated_at: str = event_data.get('updatedAt')
        self.updated_by: str = event_data.get('updatedBy')
        self.parent_list_id: str = event_data.get('parentListId')
        self.completed_at: str = event_data.get('completedAt')
        self.completed_by: str = event_data.get('completedBy')
        note = event_data.get('note')
        self.note_created_at = note.get('createdAt')
        self.note_created_by = note.get('createdBy')
        self.note_updated_at = note.get('updatedAt')
        self.note_updated_by = note.get('updatedBy')
        self.note_mentions = note.get('mentions')
        self.note_content = note.get('content')



class ListItemCreated(List):
    def __init__(self, event_data: dict):
        super().__init__(event_data)
        self.server_id: str = event_data.get('serverId')

class ListItemUpdated(List):
    def __init__(self, event_data: dict):
        super().__init__(event_data)
        self.server_id: str = event_data.get('serverId')

class ListItemDeleted(List):
    def __init__(self, event_data: dict):
        super().__init__(event_data)
        self.server_id: str = event_data.get('serverId')

class ListItemCompleted(List):
    def __init__(self, event_data: dict):
        super().__init__(event_data)
        self.server_id: str = event_data.get('serverId')


class ListItemUncompleted(List):
    def __init__(self, event_data: dict):
        super().__init__(event_data)
        self.server_id: str = event_data.get('serverId')
