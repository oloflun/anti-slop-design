// React Theme — extracted from https://aletagency.com/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '12': string;
    '36': string;
    '20.5632': string;
    '11.52': string;
    '9.6': string;
 *   };
 *   space: {
    '1': string;
    '59': string;
    '90': string;
    '154': string;
    '186': string;
    '237': string;
    '294': string;
    '320': string;
    '352': string;
    '435': string;
    '454': string;
    '474': string;
 *   };
 *   radii: {
    md: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#dc3545",
    "secondary": "#e5ddc4",
    "background": "#e5ddc4",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#252525",
    "neutral200": "#101010",
    "neutral300": "#ffffff",
    "neutral400": "#454545",
    "neutral500": "#a2a093",
    "neutral600": "#bfb5ab"
  },
  "fonts": {
    "body": "'SilkSerif-LightItalic', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "36": "36px",
    "20.5632": "20.5632px",
    "11.52": "11.52px",
    "9.6": "9.6px"
  },
  "space": {
    "1": "1px",
    "59": "59px",
    "90": "90px",
    "154": "154px",
    "186": "186px",
    "237": "237px",
    "294": "294px",
    "320": "320px",
    "352": "352px",
    "435": "435px",
    "454": "454px",
    "474": "474px"
  },
  "radii": {
    "md": "10px",
    "full": "9999px"
  },
  "shadows": {
    "sm": "rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.06) 0px 1px 2px 0px"
  },
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#dc3545",
      "light": "hsl(354, 70%, 69%)",
      "dark": "hsl(354, 70%, 39%)"
    },
    "secondary": {
      "main": "#e5ddc4",
      "light": "hsl(45, 39%, 95%)",
      "dark": "hsl(45, 39%, 68%)"
    },
    "background": {
      "default": "#e5ddc4",
      "paper": "#a2a093"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#252525"
    }
  },
  "typography": {
    "fontFamily": "'WorkSans-Regular', sans-serif",
    "h1": {
      "fontSize": "36px",
      "fontWeight": "400",
      "lineHeight": "33.84px"
    },
    "h3": {
      "fontSize": "20.5632px",
      "fontWeight": "400",
      "lineHeight": "19.3294px"
    },
    "body2": {
      "fontSize": "9.6px",
      "fontWeight": "400",
      "lineHeight": "11.04px"
    }
  },
  "shape": {
    "borderRadius": 10
  },
  "shadows": [
    "rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.06) 0px 1px 2px 0px"
  ]
};

export default theme;
