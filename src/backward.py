from torch.nn import CrossEntropyLoss

from src.utils.logger import exception_logger

@exception_logger
def backward(logits, labels, optimizer, lb_epsi=0.1, analyzer=None):
    loss = CrossEntropyLoss(label_smoothing=lb_epsi)(logits, labels)
    loss.backward()
    optimizer.step()
    if analyzer is not None:
        analyzer.add_train_val(loss.item())

    optimizer.zero_grad()
