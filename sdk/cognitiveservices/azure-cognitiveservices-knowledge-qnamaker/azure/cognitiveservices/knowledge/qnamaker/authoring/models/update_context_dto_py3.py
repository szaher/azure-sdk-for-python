# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UpdateContextDTO(Model):
    """Update Body schema to represent context to be updated.

    :param prompts_to_delete: List of prompts associated with qna to be
     deleted
    :type prompts_to_delete: list[int]
    :param prompts_to_add: List of prompts to be added to the qna.
    :type prompts_to_add:
     list[~azure.cognitiveservices.knowledge.qnamaker.authoring.models.PromptDTO]
    :param is_context_only: To mark if a prompt is relevant only with a
     previous question or not.
     true - Do not include this QnA as search result for queries without
     context
     false - ignores context and includes this QnA in search result
    :type is_context_only: bool
    """

    _attribute_map = {
        'prompts_to_delete': {'key': 'promptsToDelete', 'type': '[int]'},
        'prompts_to_add': {'key': 'promptsToAdd', 'type': '[PromptDTO]'},
        'is_context_only': {'key': 'isContextOnly', 'type': 'bool'},
    }

    def __init__(self, *, prompts_to_delete=None, prompts_to_add=None, is_context_only: bool=None, **kwargs) -> None:
        super(UpdateContextDTO, self).__init__(**kwargs)
        self.prompts_to_delete = prompts_to_delete
        self.prompts_to_add = prompts_to_add
        self.is_context_only = is_context_only