package filter

import (
	"context"

	pb "github.com/envoyproxy/go-control-plane/envoy/service/ext_proc/v3"
)

// Envoy will send the external processor ProcessingRequest messages on the bidirectional gRPC
// stream and below methods on the filter instance will get invoked. The filter
// instance can thus be stateful and maintain state to be passed around between method invocations
// eg between OnRequestHeaders and OnRequestBody.
type HttpFilter interface {
	OnRequestHeaders(context.Context, *pb.ProcessingRequest) *pb.ProcessingResponse
	OnRequestBody(context.Context, *pb.ProcessingRequest) *pb.ProcessingResponse
	OnResponseHeaders(context.Context, *pb.ProcessingRequest) *pb.ProcessingResponse
	OnResponseBody(context.Context, *pb.ProcessingRequest) *pb.ProcessingResponse
}
