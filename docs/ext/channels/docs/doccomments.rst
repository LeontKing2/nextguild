Doccomments
========

This section provides an overview of the doccomment-related methods available in the NextGuild library. The following methods are used to interact with doccomments:

create_doc_comment
------------

.. code-block:: python

    bot.create_doc_comment(channelid, docid, content)

Creates a doccomment in the specified channel.

+-------------+---------------+----------------------------------------------------+
| Parameter   | Type          | Description                                        |
+=============+===============+====================================================+
| channelid   | str           | The ID of the channel to create the doccomment in. |
+-------------+---------------+----------------------------------------------------+
| docid       | int           | The ID of the doc to create the doccomment in.     |
+-------------+---------------+----------------------------------------------------+
| content     | str           | The content of the doccomment.                     |
+-------------+---------------+----------------------------------------------------+

update_doc_comment
----------

.. code-block:: python

    bot.update_doc_comment(channelid, docid, commentid, content)

Updates a doc in the specified channel.

+-------------+---------------+---------------------------------------------+
| Parameter   | Type          | Description                                 |
+=============+===============+==================================================+
| channelid   | str           | The ID of the channel to update the comment in.  |
+-------------+---------------+--------------------------------------------------+
| docid       | int           | The ID of the doc to update the comment in.      |
+-------------+---------------+--------------------------------------------------+
| commentid   | int           | The ID of the comment to update.                 |
+-------------+---------------+--------------------------------------------------+
| title       | str           | The title of the doc.                       |
+-------------+---------------+---------------------------------------------+
| content     | str           | The content of the doc.                     |
+-------------+---------------+---------------------------------------------+

delete_doc
------------

.. code-block:: python

    bot.delete_doc(channelid, docid)

Deletes a doc in the specified channel.

+-------------+---------------+---------------------------------------------+
| Parameter   | Type          | Description                                 |
+=============+===============+=============================================+
| channelid   | str           | The ID of the channel to update the doc in. |
+-------------+---------------+---------------------------------------------+
| docid       | str           | The ID of the doc to update                 |
+-------------+---------------+---------------------------------------------+

get_doc
--------------

.. code-block:: python

    bot.delete_message(channel_id, message_id)

Retrieves a doc in the specified channel.

+-------------+---------------+---------------------------------------------+
| Parameter   | Type          | Description                                 |
+=============+===============+=============================================+
| channelid   | str           | The ID of the channel to update the doc in. |
+-------------+---------------+---------------------------------------------+
| docid       | str           | The ID of the doc to update                 |
+-------------+---------------+---------------------------------------------+

get_docs
-----------

.. code-block:: python

    bot.get_docs(channel_id)

Retrieves all the docs in the specified channel.

+-------------+---------+------------------------------------------+
| Parameter   | Type    | Description                              |
+=============+=========+==========================================+
| channel_id  | str     | The ID of the channel to retrieve the    |
|             |         | docs from.                               |
+-------------+---------+------------------------------------------+