# tasks.py
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task


@shared_task
def notify_product_update(task_id):
    # Simulate work
    import time
    time.sleep(5)

    # Send WebSocket message
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'task_updates',
        {
            'type': 'task_update',
            'data': {
                'status': 'completed',
                'task_id': task_id
            }
        }
    )
