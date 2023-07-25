#!/usr/bin/env python

"""Create clang-format config that mimics Python's black formatter style."""
import argparse

CONFIG_TEMPLATE = r"""---
Language: Cpp
AccessModifierOffset: {access_modifier_offset}
AlignAfterOpenBracket: BlockIndent
AlignArrayOfStructures: {align_array_of_structures}
AlignConsecutiveAssignments:
  Enabled: false
  AcrossEmptyLines: false
  AcrossComments: false
  AlignCompound: false
  PadOperators: false
AlignConsecutiveBitFields:
  Enabled: false
  AcrossEmptyLines: false
  AcrossComments: false
  AlignCompound: false
  PadOperators: false
AlignConsecutiveDeclarations:
  Enabled: false
  AcrossEmptyLines: false
  AcrossComments: false
  AlignCompound: false
  PadOperators: false
AlignConsecutiveMacros:
  Enabled: false
  AcrossEmptyLines: false
  AcrossComments: false
  AlignCompound: false
  PadOperators: false
AlignEscapedNewlines: Left
AlignOperands: DontAlign
AlignTrailingComments:
  Kind: {align_trailing_comments}
  OverEmptyLines: 0
AllowAllArgumentsOnNextLine: true
AllowAllParametersOfDeclarationOnNextLine: true
AllowShortBlocksOnASingleLine: Never
AllowShortCaseLabelsOnASingleLine: false
AllowShortEnumsOnASingleLine: false
AllowShortFunctionsOnASingleLine: InlineOnly
AllowShortIfStatementsOnASingleLine: Never
AllowShortLambdasOnASingleLine: All
AllowShortLoopsOnASingleLine: false
AlwaysBreakAfterReturnType: None
AlwaysBreakBeforeMultilineStrings: true
AlwaysBreakTemplateDeclarations: Yes
AttributeMacros:
  - __capability
BinPackArguments: false
BinPackParameters: false
BitFieldColonSpacing: Both
BraceWrapping:
  AfterCaseLabel: false
  AfterClass: false
  AfterControlStatement: Never
  AfterEnum: false
  AfterExternBlock: false
  AfterFunction: false
  AfterNamespace: false
  AfterObjCDeclaration: false
  AfterStruct: false
  AfterUnion: false
  BeforeCatch: false
  BeforeElse: false
  BeforeLambdaBody: false
  BeforeWhile: false
  IndentBraces: false
  SplitEmptyFunction: true
  SplitEmptyRecord: true
  SplitEmptyNamespace: true
BreakAfterAttributes: Never
BreakBeforeBinaryOperators: None
BreakBeforeConceptDeclarations: Always
BreakBeforeBraces: Attach
BreakBeforeInlineASMColon: OnlyMultiline
BreakBeforeTernaryOperators: true
BreakConstructorInitializers: BeforeColon
BreakInheritanceList: BeforeColon
BreakStringLiterals: false
ColumnLimit: {column_limit}
CommentPragmas: "^ IWYU pragma:"
CompactNamespaces: false
ConstructorInitializerIndentWidth: {indent_width}
ContinuationIndentWidth: {indent_width}
Cpp11BracedListStyle: true
DerivePointerAlignment: false
DisableFormat: false
EmptyLineAfterAccessModifier: Never
EmptyLineBeforeAccessModifier: LogicalBlock
FixNamespaceComments: true
ForEachMacros:
  - foreach
  - Q_FOREACH
  - BOOST_FOREACH
IfMacros:
  - KJ_IF_MAYBE
IncludeBlocks: Regroup
IncludeCategories:
  - Regex: '^<ext/.*\.h>'
    Priority: 2
    SortPriority: 0
    CaseSensitive: false
  - Regex: '^<.*\.h>'
    Priority: 1
    SortPriority: 0
    CaseSensitive: false
  - Regex: "^<.*"
    Priority: 2
    SortPriority: 0
    CaseSensitive: false
  - Regex: ".*"
    Priority: 3
    SortPriority: 0
    CaseSensitive: false
IncludeIsMainRegex: "([-_](test|unittest))?$"
IncludeIsMainSourceRegex: ""
IndentAccessModifiers: false
IndentCaseBlocks: false
IndentCaseLabels: true
IndentExternBlock: AfterExternBlock
IndentGotoLabels: true
IndentPPDirectives: None
IndentRequiresClause: true
IndentWidth: {indent_width}
IndentWrappedFunctionNames: false
InsertBraces: false
InsertNewlineAtEOF: false
InsertTrailingCommas: Wrapped
IntegerLiteralSeparator:
  Binary: 0
  BinaryMinDigits: 0
  Decimal: 0
  DecimalMinDigits: 0
  Hex: 0
  HexMinDigits: 0
KeepEmptyLinesAtTheStartOfBlocks: false
LambdaBodyIndentation: Signature
LineEnding: DeriveLF
MacroBlockBegin: ""
MacroBlockEnd: ""
MaxEmptyLinesToKeep: 1
NamespaceIndentation: None
ObjCBinPackProtocolList: Never
ObjCBlockIndentWidth: 2
ObjCBreakBeforeNestedBlockParam: true
ObjCSpaceAfterProperty: false
ObjCSpaceBeforeProtocolList: true
PackConstructorInitializers: NextLine
PenaltyBreakAssignment: 2
PenaltyBreakBeforeFirstCallParameter: 1
PenaltyBreakComment: 300
PenaltyBreakFirstLessLess: 120
PenaltyBreakOpenParenthesis: 0
PenaltyBreakString: 1000
PenaltyBreakTemplateDeclaration: 10
PenaltyExcessCharacter: 1000000
PenaltyIndentedWhitespace: 0
PenaltyReturnTypeOnItsOwnLine: 200
PointerAlignment: Left
PPIndentWidth: -1
QualifierAlignment: Leave
RawStringFormats:
  - Language: Cpp
    Delimiters:
      - cc
      - CC
      - cpp
      - Cpp
      - CPP
      - "c++"
      - "C++"
    CanonicalDelimiter: ""
    BasedOnStyle: google
  - Language: TextProto
    Delimiters:
      - pb
      - PB
      - proto
      - PROTO
    EnclosingFunctions:
      - EqualsProto
      - EquivToProto
      - PARSE_PARTIAL_TEXT_PROTO
      - PARSE_TEST_PROTO
      - PARSE_TEXT_PROTO
      - ParseTextOrDie
      - ParseTextProtoOrDie
      - ParseTestProto
      - ParsePartialTestProto
    CanonicalDelimiter: pb
    BasedOnStyle: google
ReferenceAlignment: Pointer
ReflowComments: {reflow_comments}
RemoveBracesLLVM: false
RemoveSemicolon: false
RequiresClausePosition: OwnLine
RequiresExpressionIndentation: OuterScope
SeparateDefinitionBlocks: Leave
ShortNamespaceLines: 1
SortIncludes: {sort_includes}
SortJavaStaticImport: Before
SortUsingDeclarations: LexicographicNumeric
SpaceAfterCStyleCast: false
SpaceAfterLogicalNot: false
SpaceAfterTemplateKeyword: true
SpaceAroundPointerQualifiers: Default
SpaceBeforeAssignmentOperators: true
SpaceBeforeCaseColon: false
SpaceBeforeCpp11BracedList: false
SpaceBeforeCtorInitializerColon: true
SpaceBeforeInheritanceColon: true
SpaceBeforeParens: ControlStatements
SpaceBeforeParensOptions:
  AfterControlStatements: true
  AfterForeachMacros: true
  AfterFunctionDefinitionName: false
  AfterFunctionDeclarationName: false
  AfterIfMacros: true
  AfterOverloadedOperator: false
  AfterRequiresInClause: false
  AfterRequiresInExpression: false
  BeforeNonEmptyParentheses: false
SpaceBeforeRangeBasedForLoopColon: true
SpaceBeforeSquareBrackets: false
SpaceInEmptyBlock: false
SpaceInEmptyParentheses: false
SpacesBeforeTrailingComments: 2
SpacesInAngles: Never
SpacesInConditionalStatement: false
SpacesInContainerLiterals: true
SpacesInCStyleCastParentheses: false
SpacesInLineCommentPrefix:
  Minimum: 1
  Maximum: -1
SpacesInParentheses: false
SpacesInSquareBrackets: false
Standard: Auto
StatementAttributeLikeMacros:
  - Q_EMIT
StatementMacros:
  - Q_UNUSED
  - QT_REQUIRE_VERSION
TabWidth: 8
UseTab: Never
WhitespaceSensitiveMacros:
  - BOOST_PP_STRINGIZE
  - CF_SWIFT_NAME
  - NS_SWIFT_NAME
  - PP_STRINGIZE
  - STRINGIZE"""


def main(args):
    """Main function"""
    config = CONFIG_TEMPLATE.format(
        access_modifier_offset=args.access_modifier_offset,
        align_array_of_structures="Always"
        if args.align_array_of_structures
        else "Never",
        align_trailing_comments="Always" if args.align_trailing_comments else "Never",
        column_limit=args.line_length,
        indent_width=args.indent_width,
        reflow_comments="true" if args.reflow_comments else "false",
        sort_includes="CaseSensitive" if args.sort_includes else "Never",
    )
    print(config)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--line-length",
        "--column-limit",  # alias
        type=int,
        help="How many characters per line to allow. [default: 88]",
        default=88,
        required=False,
    )
    parser.add_argument(
        "--indent-width",
        type=int,
        help="Indent width. [default: 4]",
        default=4,
        required=False,
    )
    # NOTE: We turned some of the options into boolean flags by making
    # an opinionated choice for the default value. This is to make the
    # script easier to use.
    parser.add_argument(
        "--align-array-of-structures",
        action="store_true",
        help="Align array of structures.",
        default=False,
        required=False,
    )
    parser.add_argument(
        "--access-modifier-offset",
        type=int,
        help="Indent width for access modifiers. [default: -2]",
        default=-2,
        required=False,
    )
    parser.add_argument(
        "--align-trailing-comments",
        action="store_true",
        help="Align trailing comments.",
        default=False,
        required=False,
    )
    parser.add_argument(
        "--reflow-comments",
        action="store_true",
        help="Reflow comments.",
        default=False,
        required=False,
    )
    parser.add_argument(
        "--sort-includes",
        action="store_true",
        help="Sort includes.",
        default=False,
        required=False,
    )

    args = parser.parse_args()
    main(args)
