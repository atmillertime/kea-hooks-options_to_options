#ifndef OPTIONS_TO_OPTIONS_H
#define OPTIONS_TO_OPTIONS_H
#include <fstream>
// "Interesting clients" log file handle declaration.

#include <log/message_initializer.h>
#include <log/macros.h>
namespace options_to_options {
extern isc::log::Logger options_to_options_logger;
extern std::string toText(const std::vector<uint8_t>& binary);
}
#endif // OPTIONS_TO_OPTIONS_H

